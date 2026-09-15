class PrivatDetector:
    @staticmethod
    def get_privat_atr(obj):
        result = []
        prefix = f"_{obj.__class__.__name__}__"

        for key, value in obj.__dict__.items():
            if key.startswith(prefix):
                attr = key[len(prefix) :]
                result.append(f"{attr} = {value}")

        return result


class Policeman:
    def __init__(self, corruption=False):
        self.__corruption = corruption
        self.eat = "donut"
        self.__iq = "Да"


pol = Policeman(corruption=True)
print(PrivatDetector.get_privat_atr(pol))
