class GameCharacter:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    @classmethod
    def create_default_character(cls):
        return cls("Guest", 1)


if __name__ == "__main__":
    vitaly = GameCharacter("Vitaly", 100)
    result1 = vitaly.create_default_character()
    result2 = GameCharacter.create_default_character()
    print(vitaly.name)  # Vitaly
    print(result1.name)  # Guest
    print(result2.name)  # Guest
