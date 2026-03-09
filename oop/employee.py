class Employee:
    company = "Stepik"

    def __init__(self, name: str, position: str):
        self.name = name
        self.position = position

    def get_info(self) -> str:
        return f"{self.name} работает в компании {self.company} на должности {self.position}."
