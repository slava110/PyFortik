class BuiltInExtension(FortikExtension):
    @property
    def id(self):
        return "built-in"

    @property
    def name(self):
        return "Built-in"

    @property
    def version(self):
        return 1

    @property
    def api_version(self):
        return 1

    @property
    def commands(self):
        return [
            FortikCommandPush(),
            FortikCommandOperation(),

        ]


class FortikCommandPush(FortikCommand):

    @property
    def name(self):
        return "push"

    def parse(self, lexem_iterator: Iterator[str]) -> FortikASTElement:
        pass

    def process(self, vm: FortikVM):
        pass


class FortikCommandOperation(FortikCommand):

    @property
    def name(self):
        return "op"

    def parse(self, lexem_iterator: Iterator[str]) -> FortikASTElement:
        pass

    def process(self, vm: FortikVM):
        pass


class FortikCommandCall(FortikCommand):

    @property
    def name(self):
        return "call"

    def parse(self, lexem_iterator: Iterator[str]) -> FortikASTElement:
        return next(lexem_iterator)

    def process(self, vm: FortikVM):
        pass


class FortikCommandIs(FortikCommand):

    @property
    def name(self):
        return "is"

    def parse(self, lexem_iterator: Iterator[str]) -> FortikASTElement:
        return next(lexem_iterator)

    def process(self, vm: FortikVM):
        pass


class FortikCommandTo(FortikCommand):

    @property
    def name(self):
        return "to"

    def parse(self, lexem_iterator: Iterator[str]) -> FortikASTElement:
        return next(lexem_iterator)

    def process(self, vm: FortikVM):
        pass


class FortikCommandExit(FortikCommand):

    @property
    def name(self):
        return "exit"

    def parse(self, lexem_iterator: Iterator[str]) -> FortikASTElement:
        pass

    def process(self, vm: FortikVM):
        pass
