class BaseSource:
    def __init__(self, obj):
        self.obj = obj

    def get_length(self):
        return len(self.obj)


class StringSource(BaseSource):
    pass


class ListSource(BaseSource):
    pass


def print_source_length(source):
    print(f"Длина источника: {source.get_length()}")
