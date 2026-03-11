class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = 0
        self.set_age(age)

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if isinstance(new_age, int) and 0 <= new_age <= 120:
            self._age = new_age
