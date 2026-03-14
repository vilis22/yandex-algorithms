class Swimmer:
    def swim(self) -> str:
        return "Я плыву"


class Walker:
    def walk(self) -> str:
        return "Я иду"


class Amphibian(Swimmer, Walker):
    pass
