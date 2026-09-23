class Woody:
    def __init__(self, damage=50, rate=0.7):
        self.damage = damage
        self.rate = rate

    def __setattr__(self, name, value):
        match name:
            case "damage":
                if not isinstance(value, int) or value <= 0:
                    raise AttributeError("Низзяяя!!!")
            case "rate":
                if not isinstance(value, (float, int)) or not (0.5 <= value <= 1.5) or round(value, 1) != value:
                    raise AttributeError("Низзяяя!!!")
        object.__setattr__(self, name, value)


class TRex:
    def __init__(self, hp=1000, speed=3):
        self.hp = hp
        self.speed = speed

    def __setattr__(self, name, value):
        match name:
            case "hp":
                if not isinstance(value, (int, float)):
                    raise AttributeError("Низзяяя!!!")
            case "speed":
                if not isinstance(value, int) or not (3 <= value <= 10):
                    raise AttributeError("Низзяяя!!!")
        object.__setattr__(self, name, value)


class Battle:
    def __init__(self, woody, trex, dist=100):
        self.woody = woody
        self.trex = trex
        self.dist = dist

    def get_result(self):
        travel_time = 0
        required_travel_time = self.dist / self.trex.speed
        shot_num = 0

        while True:
            shot_num += 1
            travel_time = (shot_num - 1) * self.woody.rate

            if travel_time >= required_travel_time:
                return "Дошел", f"Время пути: {round(required_travel_time, 1)}", f"Осталось HP: {self.trex.hp}"

            self.trex.hp -= self.woody.damage

            if self.trex.hp <= 0:
                return (
                    "Не дошел",
                    f"Убит на: {round(travel_time, 1)} сек.",
                    f"Необходимое время пути: {round(required_travel_time, 1)}",
                )
