class FullNamePersonDescriptor:
    def __set_name__(self, owner, name):
        self.f_key = f"_{name}_first"
        self.l_key = f"_{name}_last"

    def __get__(self, instance, owner):
        if instance is None:
            return self

        first = getattr(instance, self.f_key, None)
        last = getattr(instance, self.l_key, None)
        return f"{first} {last}"

    def __set__(self, instance, value):
        setattr(instance, self.f_key, value[0])
        setattr(instance, self.l_key, value[1])


class Person:
    full_name = FullNamePersonDescriptor()

    def __init__(self, first_name, last_name):
        self.full_name = (first_name, last_name)


if __name__ == "__main__":
    person = Person("Vitaly", "Zolotov")
    print(person.full_name)
