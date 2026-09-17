class SalesAmount:
    total = 0


class Descriptor:
    def __init__(self, cls):
        self.cls = cls

    def __set__(self, instance, value):
        self.cls.total += value


class Honey:
    total = Descriptor(SalesAmount)

    def __init__(self, price):
        self.price = price * 100
        self.total = self.price


print(SalesAmount.total)
honey_1 = Honey(5)
print(honey_1.__dict__)
print(SalesAmount.total)
