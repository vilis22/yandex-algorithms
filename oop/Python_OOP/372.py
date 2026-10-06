class Area:
    def __init__(self, square, people, jumper):
        self.square = square
        self.people = people
        self.jumper = jumper

    def __bool__(self):
        return self.jumper * 2 <= self.square and self.jumper * 2 <= self.people


ar_1 = Area(6, 5, 3)
print(bool(ar_1))

ar_2 = Area(6, 5, 2)
print(bool(ar_2))
