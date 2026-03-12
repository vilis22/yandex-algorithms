class Base:
    __slots__ = ("x",)

    def __init__(self, x):
        self.x = x


class Child(Base):
    pass


if __name__ == "__main__":
    child = Child(10)
    child.y = 20
    print(child.__dict__)
