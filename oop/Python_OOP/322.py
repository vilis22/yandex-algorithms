class Nikolai:
    def __init__(self, dct):
        self.atr_append(dct)

    def atr_append(self, dct):
        for key, val in dct.items():
            if key in self.__dict__:
                value = getattr(self, key)

                if isinstance(value, str):
                    setattr(self, key, [value, dct[key]])
                else:
                    value.append(dct[key])
            else:
                setattr(self, key, val)

    def __getattr__(self, item):
        raise AttributeError("Атрибут не найден")


kol = Nikolai({"глаза": "портативные", "рот": "зашит", "кожа": "с начесом", "голова": "отсутствует"})
print(kol.__dict__)
