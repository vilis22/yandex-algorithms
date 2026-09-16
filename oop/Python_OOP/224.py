from csv import DictReader


class Police:
    _WEEK = {"понедельник": 0, "вторник": 1, "среда": 2, "четверг": 3, "пятница": 4, "суббота": 5, "воскресенье": 6}

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name not in self.__parse_csv()[0]:
            raise TypeError("Такого сотрудника нет!")

        self.__name = name

    @staticmethod
    def __parse_csv():
        with open("police.csv", encoding="utf-8") as f:
            reader = DictReader(f)
            return list(reader)

    def number_arrests(self, day=None):
        if day is None:
            return sum(int(arrests[self.name]) for arrests in self.__parse_csv())

        if day.lower() not in self._WEEK:
            return "Задан некорректный день недели"

        return int(self.__parse_csv()[self._WEEK[day.lower()]][self.name])


print(Police._Police__parse_csv())
pol = Police("Махоуни")
print(pol.__dict__)
print(pol.name)

print(pol.number_arrests())
print(pol.number_arrests("вторник"))
