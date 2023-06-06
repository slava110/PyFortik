import pprint

from parser import *
from compiler import *
from decompiler import *


fortik_parser = FortikParser()

ast_tree = fortik_parser.parseToAST(iter("""
[ to n n 2 < [ 1 ] [ n n 1 - fact * ] if ] is fact
5 fact .
"""))

pprint.pp(ast_tree)

fortik_compiler = FortikCompiler()

compiled = fortik_compiler.compile_to_bytecode(ast_tree)

print("Compiled")
pprint.pp(compiled)

fortik_decompiled = FortikDecompiler()

print("Decompiled")
fortik_decompiled.decompile(compiled)