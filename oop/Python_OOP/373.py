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
