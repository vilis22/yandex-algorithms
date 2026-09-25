class Medovik:
    def __init__(self, pieces=12):
        self._pieces = pieces

    @property
    def pieces(self):
        return self._pieces

    @pieces.setter
    def pieces(self, value):
        if value < 0:
            raise TypeError("Низзяяя!!!")

        self._pieces = value

    def __str__(self):
        if self._pieces == 0:
            return "Здесь был медовичок(("

        return f"{self._pieces} куск."

    def __sub__(self, other):
        if self._pieces - other < 0:
            raise TypeError("Низзяяя!!!")

        return Medovik(self.pieces - other)

    def __rsub__(self, other):
        if other - self._pieces < 0:
            raise TypeError("Низзяяя!!!")

        return Medovik(other - self.pieces)


med = Medovik()
print(med.__dict__, med.pieces)
med.pieces = 14
print(med.__dict__, med.pieces)

try:
    med.pieces = -8
except TypeError as e:
    print(e)

print(med)

med = med - 6
print(med)

med = 15 - med
print(med)

try:
    med = 6 - med
except TypeError as e:
    print(e)

print(med - 7, 7 - med)
