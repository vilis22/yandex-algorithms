class Shape:
    def describe(self):
        return "Это общая фигура"


class Circle(Shape):
    def describe(self):
        return "Это круг"


class Square(Shape):
    def describe(self):
        return "Это квадрат"


def get_shape_type(shape_object):
    if hasattr(shape_object, "describe"):
        return shape_object.describe()
