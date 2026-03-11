class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        return "Двигатель запущен"

    def honk(self):
        return "Общий сигнал!"


class Car(Vehicle):
    def start_engine(self):
        super().start_engine()
        return "Двигатель запущен... Проверка систем автомобиля."

    def honk(self):
        return "Би-бип!"
