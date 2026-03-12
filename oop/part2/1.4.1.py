class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


if __name__ == "__main__":
    v1 = Vector(10, 20)
    v2 = Vector(3, 7)
    print(v1 + v2)
    print(v1 + 2)
