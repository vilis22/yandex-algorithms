class Engine:
    def start(self):
        return "Двигатель запущен"


class Wheels:
    def rotate(self):
        return "Колеса вращаются"


class Car:
    def __init__(self):
        self.engine = Engine()
        self.wheels = Wheels()

    def drive(self):
        return f"{self.engine.start()} и {self.wheels.rotate()}"
