class Descriptor:
    def __set_name__(self, owner, name):
        self.name = f"_{owner.__name__}__{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self

        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if len(value) > 10:
            raise TypeError("Низзяяя!!!")

        setattr(instance, self.name, value)


class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)

        if len(args[0].carriages) > 10:
            raise TypeError("Мистер декоратор против!!!")

        return result


class CrazyTrain:
    carriages = Descriptor()

    def __init__(self, carriages) -> None:
        self.carriages = carriages

    def __iadd__(self, other):
        self.__carriages.extend(other.carriages)
        return self


train1 = CrazyTrain([[1], [2], [1], [2], [1], [2], [1], [2], [1], [2]])
train2 = CrazyTrain([[3]])

train1 += train2

print(train1.carriages)
