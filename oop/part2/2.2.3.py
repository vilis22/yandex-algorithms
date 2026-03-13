class Circle:
    def __init__(self, radius):
        if self._is_valid_radius(radius):
            self.radius = radius
        else:
            raise ValueError("Некорректный радиус")

    @staticmethod
    def _is_valid_radius(radius):
        try:
            return radius > 0
        except TypeError:
            pass


if __name__ == "__main__":
    circle = Circle("5")
