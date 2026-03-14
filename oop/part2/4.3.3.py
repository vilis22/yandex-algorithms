class ValidatedString:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name, None)

    def __set__(self, instance, value):
        if isinstance(value, str):
            setattr(instance, self.private_name, value)
        else:
            raise TypeError
