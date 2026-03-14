class ConstantDescriptor:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        raise AttributeError


class MyClass:
    PI = ConstantDescriptor(3.14159)


if __name__ == "__main__":
    obj = MyClass()
    print(obj.PI)
    obj.PI = 5
