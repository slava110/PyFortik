from typing import List

from ast_util import FortikASTBlock, FortikASTWalker
from opcodes import commands, operators


class FortikCompiler:

    def compile_to_bytecode(self, ast: FortikASTBlock) -> list[int]:
        procedures_bytecode: List[int] = list()

        callable_names: dict[str, int] = dict()
        next_callable_name_index: int = 0

        scope = CompilationScope(ast.__iter__())

        while True:
            deeper = False
            for (cmd, arg) in scope.ast_walker:
                if cmd == 'push' and isinstance(arg, list):
                    scope.encode_cmd(cmd, len(procedures_bytecode))

                    scope = scope.child(arg.__iter__())
                    deeper = True
                    break
                elif cmd == 'to' or cmd == 'is' or cmd == 'call':
                    if arg in callable_names:
                        scope.encode_cmd(cmd, callable_names[arg])
                    else:
                        callable_names[arg] = next_callable_name_index
                        scope.encode_cmd(cmd, next_callable_name_index)
                        next_callable_name_index = next_callable_name_index + 1
                elif cmd == 'op':
                    scope.encode_cmd(cmd, list(operators.keys()).index(arg))
                else:
                    scope.encode_cmd(cmd, arg)

            if not deeper:
                scope.bytecode.append(5)
                if scope.parent is not None:
                    procedures_bytecode.extend(scope.bytecode)
                    scope = scope.parent
                else:
                    break

        return [len(procedures_bytecode)] + procedures_bytecode + scope.bytecode


class CompilationScope:

    def __init__(self, ast_walker: FortikASTWalker, parent: 'CompilationScope' = None):
        self.ast_walker = ast_walker
        self.parent = parent
        self.bytecode: List[int] = list()

    def encode_cmd(self, cmd: str, arg: int):
        print(f"Encoding { cmd }({ arg })")
        print(f"> { commands.index(cmd) | (arg << 3) }")
        self.bytecode.append(commands.index(cmd) | (arg << 3))

    def child(self, ast_walker: FortikASTWalker) -> 'CompilationScope':
        return CompilationScope(parent=self, ast_walker=ast_walker)
