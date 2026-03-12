class FlexibleObject:
    __slots__ = ("fixed_attribute", "__dict__")

    def __init__(self, value):
        self.fixed_attribute = value


if __name__ == "__main__":
    player = FlexibleObject(10)
    player.y = 20
    print(player.__slots__)
    print(player.__dict__)
