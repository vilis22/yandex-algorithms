from typing import Any, Self


class Pizza:
    def __init__(self, pieces: int) -> None:
        self._validate(pieces)
        self._pieces = [pieces]

    def _validate(self, pieces: Any) -> None:
        if not (isinstance(pieces, int) and 0 <= pieces <= 8):
            raise TypeError("Низзяяя!!!")

    def __ior__(self, other: int) -> Self:
        if not isinstance(other, int):
            raise TypeError("Низзяяя!!!")

        self._validate(self._pieces[0] + other)
        self._pieces[0] += other
        return self

    def __bool__(self) -> bool:
        return self._pieces != [0]


pizza = Pizza(0)
print(pizza.__dict__)

try:
    pizza = Pizza('0')
except TypeError as e:
    print(e)

try:
    pizza._pieces = []
except TypeError as e:
    print(e)

try:
    pizza.__setattr__('_pieces', {})
except TypeError as e:
    print(e)

pizza |= 1
print(pizza._pieces)

pizza |= 3
print(pizza._pieces)

try:
    pizza |= '4'
except TypeError as e:
    print(e)

print(bool(pizza))
pizza |= 3
print(pizza._pieces, bool(pizza))

pizza = Pizza(0)
print(bool(pizza))