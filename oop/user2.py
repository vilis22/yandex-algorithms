class User:
    def __init__(self):
        self._age: int = 0

    def get_age(self) -> int:
        return self._age

    def set_age(self, new_age: int):
        if isinstance(new_age, int) and new_age >= 0:
            self._age = new_age
