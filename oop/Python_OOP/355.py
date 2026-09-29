class Descriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self

        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise TypeError("Низзяяя!!!")

        instance.__dict__[self.name] = value


class Screw:
    number_revol = Descriptor()

    def __init__(self, number_revol):
        self.number_revol = number_revol
        self.free_revol = number_revol

    def __str__(self):
        return f"Шуруп завернут на {self.number_revol - self.free_revol} об., осталось - {self.free_revol} об."

    def __call__(self, screw_turns):
        self.free_revol -= screw_turns
        return self

    def __eq__(self, other):
        return self.free_revol == other.free_revol

    def __lt__(self, other):
        return self.free_revol < other.free_revol

    def __le__(self, other):
        return self.free_revol <= other.free_revol
