class SpiceBase:
    def __init__(self):
        self.lst = [0] * 10

    def __str__(self):
        return str(self.lst)

    def __len__(self):
        return sum(self.lst)

    def __add__(self, other):
        if len(self) + other > 10000:
            raise TypeError("Низзяяя!!!")

        i = 0

        while other > 0:
            free = 1000 - self.lst[i]

            if not free:
                i += 1
                continue

            if free >= other:
                self.lst[i] += other
                other = 0
            else:
                self.lst[i] = 1000
                other -= free
                i += 1

        return self

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if len(self) - other < 0:
            raise TypeError("Низзяяя!!!")

        i = 0

        while other > 0:
            if self.lst[i] <= other:
                other -= self.lst[i]
                self.lst[i] = 0
                i += 1
            else:
                self.lst[i] -= other
                return self

        return self

    def __rsub__(self, other):
        return self.__sub__(other)


sb = SpiceBase()
print(sb, sb.__dict__, len(sb), sep="\n")

sb = sb + 2666
print(sb, len(sb))

sb = 4777 + sb
print(sb, len(sb))

try:
    sb = sb + 3000
except TypeError as e:
    print(e)

# sb = sb + 1443 * (-1)
sb = sb - 1443
print(sb, len(sb))

sb = 3562 - sb
print(sb, len(sb))

try:
    sb = 2534 - sb
except TypeError as e:
    print(e)

print(sb, sb.__dict__, len(sb), sep="\n")
