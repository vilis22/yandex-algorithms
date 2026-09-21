class Lift:
    def __init__(self, a, b):
        self.floors = tuple(floor for floor in range(a, b + 1) if floor != 0)
        self.lst = []

    def __len__(self):
        return len(self.floors)

    def get_drive(self, departure, purpose):
        if departure not in self.floors or purpose not in self.floors:
            raise ValueError("Низзяяя!!!")

        if len(self.lst) == 3:
            del self.lst[0]

        self.lst.append((departure, purpose))

    def __abs__(self):
        return [abs(b - a) - 1 if a < 0 and b > 0 or a > 0 and b < 0 else abs(b - a) for a, b in self.lst]


lift = Lift(-15, 37)
print(lift.__dict__)
print(len(lift))

lift.get_drive(1, 6)
print(lift.lst)
print(abs(lift))

lift.get_drive(-15, -7)
print(lift.lst)
print(abs(lift))

lift.get_drive(-7, 16)
print(lift.lst)
print(abs(lift))

lift.get_drive(25, 5)
print(lift.lst)
print(abs(lift))
