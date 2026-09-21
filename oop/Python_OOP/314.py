class City:
    def __init__(self, indicators):
        districts = ("пармезан", "усы", "карась", "дубки", "литр", "техас", "скибиди")
        self.__dct = dict(zip(districts, indicators))

    def __abs__(self):
        return {district: abs(indicator) for district, indicator in self.__dct.items()}

    def get_happy_level(self, public=True):
        updated_dct = {key: min(val + 3, 10) for key, val in abs(self).items()} if public else self.__dct
        average = sum(updated_dct.values()) / len(updated_dct)
        return average


lucky_city = City((9, 5, 0, -3, -5, -7, -6))
print(lucky_city.__dict__)
print(abs(lucky_city))
print(lucky_city.get_happy_level())
print(lucky_city.get_happy_level(False))
