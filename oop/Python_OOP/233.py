class Devices:
    lst_dev = []

    def __init__(self, name, traffic):
        self.name = name
        self.traffic = traffic
        self.__add_dev(self)

    @classmethod
    def __add_dev(cls, device):
        """Добавляет девайс в список."""
        cls.lst_dev.append(device)

    @classmethod
    def remove_dev(cls, device):
        """Удаляет девайс из списка."""
        cls.lst_dev.remove(device)

    @classmethod
    def general_traff_dev(cls):
        return sum(device.traffic for device in cls.lst_dev)


class Descriptor:
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        instance.__dict__[self.name] = (instance.spd_int - value) >= 30


class Stream:
    flag = Descriptor()

    def __init__(self, traffic_load, spd_int=100):
        self.traffic_load = traffic_load
        self.spd_int = spd_int
        self.flag = traffic_load
