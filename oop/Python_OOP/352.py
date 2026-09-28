class Employee:
    _count = 0
    _COEFS = {1: 1.3, 2: 1.6, 3: 1.9, 4: 2.2}

    def __init__(self, cat=1, base=50000):
        self.zp = self._get_zp(cat, base)
        self.__class__._count += 1

    def _get_zp(self, cat, zp):
        if cat not in self._COEFS:
            raise TypeError("Категория не найдена!")

        return int(self._COEFS[cat] * zp)

    @classmethod
    def get_count(cls):
        return f"Сотрудников в компании - {cls._count}"

    def __eq__(self, other):
        return self.zp == other.zp

    def __lt__(self, other):
        return self.zp < other.zp

    def __le__(self, other):
        return self.zp <= other.zp


emp_1 = Employee()
print(emp_1.__dict__)
emp_2 = Employee(2, 55000)
print(emp_2.__dict__)
print(emp_1 <= emp_2)
