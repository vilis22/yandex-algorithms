class Turtle:
    def __init__(self):
        self.speed = 1

    def nitro(self):
        return self.speed * 3, 5


class Track:
    def __init__(self, distance):
        self.distance = distance

    def timing(self, turtle, number):
        time_nitro = turtle.nitro()[1] * number
        distance_nitro = turtle.nitro()[0] * time_nitro
        return self.distance - distance_nitro + time_nitro


turtle = Turtle()
print(turtle.__dict__)
print(turtle.nitro())

tr_1 = Track(50)
print(tr_1.timing(turtle, 0))
print(tr_1.timing(turtle, 1))
print(tr_1.timing(turtle, 2))

tr_2 = Track(150)
print(tr_2.timing(turtle, 5))
print(tr_2.timing(turtle, 9))
print(tr_2.timing(turtle, 3))
