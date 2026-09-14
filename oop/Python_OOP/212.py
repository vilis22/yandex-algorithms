class Superhero:
    pass


class Man:
    def __init__(self, is_superhero):
        self.__superhero = is_superhero

    def turning_into_superhero(self):
        return Superhero() if self.__superhero else self
