class Device:
    def power_on(self):
        return "Устройство включено"


class Computer(Device):
    def power_on(self):
        return "Компьютер загружается..."
