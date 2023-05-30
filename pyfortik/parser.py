from itertools import groupby
from typing import Iterator
from ast_util import FortikASTBlock, FortikASTElement
import opcodes


def determine_char_group(c: str) -> int:
    if c == '\n' or c == '\r\n':
        return 1
    elif c.isspace():
        return 2
    else:
        return 0


def iterate_over_lexems(char_iterator: Iterator[str]) -> Iterator[tuple[tuple[int, int], str]]:
    line_num = 1
    char_num = 1
    for group_type, g in groupby(char_iterator, determine_char_group):
        match group_type:
            case 0:
                lexem = ''.join(g)
                yield (line_num, char_num), lexem
                char_num += len(lexem)
            case 1:
                line_num += 1
                char_num = 1
            case 2:
                char_num += sum(1 for _ in g)


class FortikParser:

    def parseToAST(self, char_iterator: Iterator[str]) -> FortikASTBlock:
        parsing_scope = ParsingScope()

        lexem_iterator = iterate_over_lexems(char_iterator)

        for pos, lexem in lexem_iterator:
            if lexem.isdigit():
                parsing_scope.command('push', int(lexem))
            elif lexem == '[':
                child = parsing_scope.child(pos)
                parsing_scope.command('push', child.ast_tree)
                parsing_scope = child
            elif lexem == ']':
                prev_scope = parsing_scope.parent
                if prev_scope is None:
                    raise ParsingError(f'Redundant closing bracket at line {pos[0]} character {pos[1]}')
                parsing_scope = prev_scope
            elif lexem == 'is' or lexem == 'to':
                arg = next(lexem_iterator, None)[1]
                if arg is None:
                    raise ParsingError(f'Expected variable name at line {pos[0]} character {pos[1]}')
                parsing_scope.command(lexem, arg)
            elif lexem in opcodes.operators.keys():
                parsing_scope.command('op', lexem)
            else:
                parsing_scope.command('call', lexem)

        if parsing_scope.parent is not None:
            raise ParsingError(f'Unclosed bracket at line {parsing_scope.pos_in_parent[0]}'
                               f'character {parsing_scope.pos_in_parent[1]}!')

        return parsing_scope.ast_tree


class ParsingScope:

    def __init__(
            self,
            parent: 'ParsingScope' = None,
            pos_in_parent: tuple[int, int] = None
    ):
        self.ast_tree = list()
        self.parent = parent
        self.pos_in_parent = pos_in_parent

    def command(self, name: str, arg: FortikASTElement):
        self.ast_tree.append((name, arg))

    def child(self, pos: tuple[int, int]):
        return ParsingScope(parent=self, pos_in_parent=pos)


class ParsingError(Exception):
    pass
