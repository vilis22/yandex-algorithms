class DaySurvival:
    dct = {"ветки": 10, "крупные листья": 30, "вода": 1.5, "обувь": 1, "продукты": 3, "средство самозащиты": 1}

    @classmethod
    def will_the_day_last(cls, bag):
        return all(bag.get(item, 0) >= amount for item, amount in cls.dct.items())
