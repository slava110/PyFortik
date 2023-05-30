import pprint

from parser import *


parser = FortikParser()

ast_tree = parser.parseToAST(iter("""
[ to n  n 2 < [ 1 ] [ n n 1 - fact * ] if ] is fact
5 fact .
"""))

pprint.pp(ast_tree)