class Base:
    def get_info(self):
        return "Base"


class Left(Base):
    def get_info(self):
        return super().get_info() + "-Left"


class Right(Base):
    def get_info(self):
        return super().get_info() + "-Right"


class Child(Left, Right):
    def get_info(self):
        return super().get_info() + "-Child"


print(Child.__mro__)
print(Child().get_info())
