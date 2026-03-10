class Component:
    def __init__(self, name: str, version: str, _id: int) -> None:
        self.name = name
        self._id = _id
        self.__version = version
