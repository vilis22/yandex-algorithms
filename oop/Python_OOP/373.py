from typing import Any, Self


class Pizza:
    def __init__(self, pieces: int) -> None:
        self._pieces = [pieces]

    @staticmethod
    def _validate(value: Any) -> None:
        if not isinstance(value, list) or len(value) != 1:
            raise TypeError("Низзяяя!!!")

        piece = value[0]

        if not isinstance(piece, int) or isinstance(piece, bool) or not 0 <= piece <= 8:
            raise TypeError("Низзяяя!!!")

    def __setattr__(self, name: str, value: Any) -> None:
        if name == "_pieces":
            self._validate(value)

        super().__setattr__(name, [value[0]])

    def __ior__(self, other: int) -> Self:
        if not isinstance(other, int) or isinstance(other, bool):
            raise TypeError("Низзяяя!!!")

        new_value = self._pieces[0] + other
        self._validate([new_value])

        self._pieces[0] = new_value
        return self

    def __bool__(self) -> bool:
        return self._pieces != [0]
