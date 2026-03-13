class CPU:
    def calculate(self):
        return "Вычисления..."


class Computer:
    def __init__(self):
        self.cpu = CPU()

    def run(self):
        return self.cpu.calculate()
