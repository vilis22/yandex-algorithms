class Worker:
    def __init__(self) -> None:
        self.__salary = 50000

    def get_info(self) -> str:
        return f"Зарплата: {self.__salary}"
