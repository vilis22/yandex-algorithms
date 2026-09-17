class Descriptor:
    dct = {
        "Крыса": "готовить рататуй",
        "Бык": "бычить",
        "Тигр": "одиноко рычать в поле",
        "Кот": "драть диван",
        "Дракон": "пламя из всех щелей",
        "Змея": "поступить в Слизерин",
        "Лошадь": "делать игого",
        "Коза": "воровать капусту",
        "Обезьяна": "корчить мосю",
        "Петух": "хвалиться шмотом",
        "Собака": "любить ноги",
        "Свинья": "резвиться в луже",
    }
    dct_lower = {key.lower(): value for key, value in dct.items()}

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        """Получает значение."""
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        """Проводит валидацию при установке значения."""
        if self.name == "zodiac":
            if value.lower() not in self.dct_lower:
                raise TypeError("Низзяяя!!!")

            instance.__dict__["zodiac"] = value
            instance.__dict__["ability"] = self.dct_lower[value.lower()]


class Zodiac:
    zodiac = Descriptor()
    ability = Descriptor()

    def __init__(self, zodiac):
        self.zodiac = zodiac


zod = Zodiac("лошадь")
print(zod.__dict__)
