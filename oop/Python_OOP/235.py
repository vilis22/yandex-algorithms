class Descriptor:
    def __set__(self, instance, value):
        if value:
            instance.__dict__["form"] = "волк"
            instance.__dict__["hp"] = 500
        else:
            instance.__dict__["form"] = "человек"
            instance.__dict__["hp"] = 50


class WolfOrHuman:
    status = Descriptor()

    def __init__(self, status):
        self.status = status


d = WolfOrHuman(True)
print(d.__dict__)
