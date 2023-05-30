from typing import Iterator

from api import FortikParserRule, ParsingError, ParsingScope


class FortikParserRuleCodeBlock(FortikParserRule):

    def matches(self, lexem_pos: tuple[int, int], lexem: str):
        return lexem == '[' or lexem == ']'

    def process_lexem(
            self,
            lexem_pos: tuple[int, int],
            lexem: str,
            lexem_iterator: Iterator[tuple[int, str]],
            scope: ParsingScope
    ) -> ParsingScope:
        if lexem == '[':
            child = scope.child(lexem_pos)
            scope.command('push', child.ast)
            return child
        else:
            if scope.parent is None:
                raise ParsingError(f'Redundant closing bracket at line {lexem_pos[0]} character {lexem_pos[1]}')
            return scope.parent


class FortikParserRuleNumber(FortikParserRule):

    def matches(self, lexem_pos: tuple[int, int], lexem: str):
        return lexem.isdigit()

    def process_lexem(
            self,
            lexem_pos: tuple[int, int],
            lexem: str,
            lexem_iterator: Iterator[tuple[tuple[int, int], str]],
            scope: ParsingScope
    ) -> ParsingScope:
        num_info = next(lexem_iterator, None)
        if num_info is None:
            raise ParsingError(f'Expected number at line {lexem_pos[0]} character {lexem_pos[1]}')
        if not num_info[1].isdigit():
            raise ParsingError(f'Expected number at line {num_info[0][0]} character {num_info[0][1]}')

        scope.command('push', int(num_info[1]))
        return scope


class FortikParserRuleCommand(FortikParserRule):

    def __init__(self, commands: dict[str, FortikCommand]):
        self.commands = commands

    def matches(self, lexem_pos: tuple[int, int], lexem: str):
        return lexem in self.commands.keys()

    def process_lexem(
            self,
            lexem_pos: tuple[int, int],
            lexem: str,
            lexem_iterator: Iterator[tuple[tuple[int, int], str]],
            scope: ParsingScope
    ) -> ParsingScope:
        TODO
        return scope