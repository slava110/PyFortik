from opcodes import commands, operators


class FortikDecompiler:

    def decompile(self, bytecode: list[int]):
        if not bytecode:
            return

        entry_point = bytecode[0]

        i = 1

        while i < len(bytecode):
            if i == entry_point:
                print("Entry:")
            else:
                encoded = bytecode[i]
                cmd = commands[encoded & 0b111]
                arg = encoded >> 3
                print(f"\t{commands[encoded & 0b111]}({ list(operators.keys())[arg] if cmd == 'op' else arg })")
            i = i + 1
