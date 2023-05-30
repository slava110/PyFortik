from typing import Union

FortikASTElement = Union['FortikASTBlock', int, str]

FortikASTBlock = list[tuple[str, FortikASTElement]]
