class Nikita:
    def __init__(self):
        self.fullness = 0

    def __iadd__(self, other):
        if isinstance(other, Nikita):
            raise TypeError("Эй, я не пью себе подобных!")

        self.fullness += other.volume
        return self


class Milk:
    def __init__(self, volume):
        self.volume = volume


nik_1 = Nikita()
id_nik = id(nik_1)
print(nik_1.__dict__)
milk_1 = Milk(15)
print(milk_1.__dict__)
nik_1 += milk_1
print(nik_1.__dict__, id_nik == id(nik_1))

milk_2 = Milk(26)
nik_1 += milk_2
print(nik_1.__dict__, id_nik == id(nik_1))

nik_2 = Nikita()
try:
    nik_1 += nik_2
except TypeError as e:
    print(e)
