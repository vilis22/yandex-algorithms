class Jellyfish:
    def __init__(self, name, nickname=None):
        self.name = name
        self.__nickname = nickname

    def get_name(self):
        return self.name

    def get_nickname(self, obj):
        if obj.name == "Валера":
            return self.__nickname
        else:
            return "Не скажу"


jel_1 = Jellyfish("Алена", "автономный биомодуль")
print(jel_1.get_name())
print(jel_1._Jellyfish__nickname)
jel_2 = Jellyfish("Швепс")
print(jel_2.__dict__)
jel_3 = Jellyfish("Валера", "Хрутка")
print(jel_1.get_nickname(jel_2))
print(jel_1.get_nickname(jel_3))
