class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age

    def get_info(self) -> str:
        return f"Имя: {self.username}, Возраст: {self.age}"
