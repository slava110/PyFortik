from typing import List, Iterator

from ast_util import FortikASTBlock, FortikASTElement


class FortikCompiler:

    def compile_to_bytecode(self, ast: FortikASTBlock) -> list[int]:
        bytecode: List[int] = list()

        procedures_bytecode: List[int] = list()
        procedures_indicies: dict[str, int] = dict()
        next_procedure_index: int = -1

        scope = CompilationScope(ast.__iter__(), None)

        to_process = [ast]

        while scope is not None:
            for (cmd, arg) in scope.ast_walker:
                if arg is FortikASTBlock:
                    self.encode_cmd(bytecode, 'push', len(procedures_bytecode))
                    procedures_bytecode.append()
                    break
                elif cmd == 'is':
                    self.encode_cmd(bytecode, cmd, )
                scope = scope.parent
            bytecode.append(5)

        return bytecode

    def encode_cmd(self, bytecode: list[int], cmd: str, arg: int):
        pass
        # self.add_cmd(bytecode, cmd, arg)


class CompilationScope:

    def __init__(self, ast_walker: Iterator[tuple[str, FortikASTElement]], parent: 'CompilationScope' = None):
        self.ast_walker = ast_walker
        self.parent = parent
