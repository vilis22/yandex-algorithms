class Shape:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color


class Polygon(Shape):
    def __init__(self, color, num_sides):
        super().__init__(color)
        self.num_sides = num_sides


class Square(Polygon):
    def __init__(self, color, side_length):
        super().__init__(color, num_sides=4)
        self.side_length = side_length
