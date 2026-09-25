class MagicBox:
    def __init__(self, key):
        self.box = {key: []}

    @property
    def key(self):
        return next(iter(self.box))

    def __str__(self):
        return str(self.box[self.key])

    def __add__(self, other):
        self.box[self.key].extend([other] * self.key)
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def __truediv__(self, other):
        new_len = len(self.box[self.key]) // other
        self.box[self.key] = self.box[self.key][-new_len:]
        return self


mb = MagicBox(5)
mb_id = id(mb)
print(mb, mb.__dict__)
mb = mb + "гидрохрюша"
print(mb)
mb = 7 + mb
print(mb)

mb = mb / 2
print(mb)
print(mb_id == id(mb))

mb = MagicBox(4)
mb_id = id(mb)
mb = mb + "гидрохрюша" + 7 + "утка-гармонист"
print(mb)
mb = mb / 2
print(mb)
mb = mb + ["я в квадратике))"]
print(mb)
mb = mb / 3
print(mb)
print(mb_id == id(mb))
