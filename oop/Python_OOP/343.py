class Descriptor:
    def __set_name__(self, owner, name):
        self.private_name = f"_{owner.__name__}__{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.private_name, [])

    def __set__(self, instance, value):
        if len(value) > 10:
            raise TypeError("Низзяяя!!!")

        instance.__dict__[self.private_name] = value


class CrazyTrain:
    carriages = Descriptor()

    def __init__(self, carriages) -> None:
        self.carriages = carriages

    def __iadd__(self, other):
        self.carriages.extend(other.carriages)
        return self


lst = [["тушенка из Василия"], ["крыжовник"], ["морковный треш"], ["шерстяные лужи"], ["сонный димдимыч"]]
crazy_tr = CrazyTrain(lst)

print(crazy_tr.__dict__)
print(crazy_tr.carriages)
del crazy_tr._CrazyTrain__carriages
print(crazy_tr.__dict__)
