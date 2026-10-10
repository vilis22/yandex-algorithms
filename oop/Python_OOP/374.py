from typing import Any


def decor(method):
    allowed_speeds = [100, 250, 500, 750, 1000]

    def wrapper(self, name: str, value: Any) -> None:
        if name == "speed" and value not in allowed_speeds:
            raise TypeError("Скорость интернета можно менять только на эти числа - [100, 250, 500, 750, 1000]")

        object.__setattr__(self, name, value)

    return wrapper


class Internet:
    def __init__(self, speed: int = 100) -> None:
        self.speed = speed

    def __setattr__(self, name: str, value: Any) -> None:
        if name == "speed" and hasattr(self, "speed"):
            raise TypeError("Скорость интернета менять нельзя!!!")

        super().__setattr__(name, value)
