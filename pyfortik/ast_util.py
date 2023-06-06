from typing import Union, Iterator

FortikASTElement = Union['FortikASTBlock', int, str]

FortikASTBlock = list[tuple[str, FortikASTElement]]

FortikASTWalker = Iterator[tuple[str, FortikASTElement]]