class Schoolchild:
    def __init__(self, biceps):
        self.biceps = biceps

    def __eq__(self, other):
        return self.biceps == other.biceps

    def __lt__(self, other):
        return self.biceps < other.biceps

    def __le__(self, other):
        return self.biceps <= other.biceps


sc_1 = Schoolchild(34)
sc_2 = Schoolchild(22)
print(sc_1 == sc_2)
print(sc_1 != sc_2)
print(sc_1 < sc_2)
print(sc_1 <= sc_2)
print(sc_1 > sc_2)
print(sc_1 >= sc_2)
