from typing import Any


class Shoe:
    def __init__(self) -> None:
        self.__counter = 0

    def __call__(self, *args: Any, **kwds: Any) -> str:
        self.__counter += 1

        if self.__counter <= 100:
            return "ну впринципе еще свежачок"

        if self.__counter <= 200:
            return "там, что скунс взорвался?"

        return "Боже! Вонь невероятная. Ещё!"
