from typing import Any


class Brutforce:
    def __init__(self, func) -> None:
        self.__func = func

    def __call__(self, *args: Any, **kwds: Any) -> tuple[str, str] | None:
        for password_num in range(1, 1000000):
            try:
                password_str = f"{password_num:06d}"
                self.__func(password_str)
                return ("Секретная информация", password_str)
            except TypeError:
                pass


@Brutforce
def func(code):
    if code == "999999":
        return "Секретная информация"
    raise TypeError("Низзяяя!!!")


print(func())
