class Smartphone:
    capacity = 3000

    def __init__(self, charge_level):
        self.charge_level = charge_level

    @classmethod
    def set_capacity(cls, capacity):
        cls.capacity = capacity


class Charger:
    def __init__(self, amperage):
        self.amperage = amperage

    def time_charging(self, smartphone: Smartphone):
        unfilled_capacity = smartphone.capacity * (100 - smartphone.charge_level) / 100
        t = 1.4 * unfilled_capacity / self.amperage / 1000 * 60
        return f"{int(t) // 60} ч. {int(t) % 60} мин."
