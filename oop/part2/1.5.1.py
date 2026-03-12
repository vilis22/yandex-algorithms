class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        PI = 3.14159
        return PI * self._radius**2
