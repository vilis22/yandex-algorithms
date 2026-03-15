class InvalidAgeError(ValueError):
    pass


class Person:
    def __init__(self, name, age):
        if age < 0:
            raise InvalidAgeError("Возраст не может быть отрицательным")

        self.name = name
        self.age = age
