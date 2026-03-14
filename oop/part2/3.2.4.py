class ReprMixin:
    def __repr__(self):
        attrs = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items() if not k.startswith("_"))
        return f"{type(self).__name__}({attrs})"


class SomeClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class PrettyClass(ReprMixin, SomeClass):
    pass
