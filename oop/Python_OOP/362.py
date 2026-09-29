class Decorator:
    def __init__(self, func):
        self.func = func

    @staticmethod
    def compot(func):
        forbidden = {"стекловата", "Васька", "нло", "револьвер"}

        def wrapper(self, ingredients, *args, **kwargs):
            if any(item in forbidden for item in ingredients):
                raise TypeError("Низзяяя!!!")

            return func(self, ingredients, *args, **kwargs)

        return wrapper


class InMouthCompote:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __hash__(self):
        return hash(tuple(sorted(self.ingredients)))

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()


comp_1 = InMouthCompote(["вода", "малина", "уран", "сахар"])
comp_2 = InMouthCompote(["малина", "вода", "сахар", "уран"])

print(comp_1 == comp_2)
print(hash(comp_1) == hash(comp_2))

comp_3 = InMouthCompote(["вода", "сварочный аппарат", "повидло", "сахар"])
comp_4 = InMouthCompote(["вода", "сварочный аппарат", "повидло", "шмель"])

print(comp_3 == comp_4)
print(hash(comp_3) == hash(comp_4))

InMouthCompote.__init__ = Decorator.compot(InMouthCompote.__init__)

try:
    comp_5 = InMouthCompote(["гренки", "нло", "вода", "сахар"])
except TypeError as e:
    print(e)
comp_6 = InMouthCompote(["вода", "руберойд", "сахар", "вишня"])

try:
    comp_7 = InMouthCompote(["Колыван", "вода", "сахар", "револьвер"])
except TypeError as e:
    print(e)

comp_8 = InMouthCompote(["подозрительные шарики", "вода", "сникерс", "сахар"])
comp_9 = InMouthCompote(["сахар", "зарин", "бубаляка", "вода"])
print(comp_8 == comp_9)
print(hash(comp_8) == hash(comp_9))

comp_10 = InMouthCompote(["акулий мозжечок", "вода", "сахар", "филе филина"])
comp_11 = InMouthCompote(["вода", "акулий мозжечок", "филе филина", "сахар"])
print(comp_10 == comp_11)
print(hash(comp_10) == hash(comp_11))
