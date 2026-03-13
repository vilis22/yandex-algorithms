class PetrolEngine:
    def start(self) -> str:
        return "Бензиновый двигатель запущен"


class ElectricEngine:
    def start(self) -> str:
        return "Электрический двигатель активирован"


class Car:
    def __init__(self, model: str, engine: PetrolEngine | ElectricEngine) -> None:
        self.model = model
        self.engine = engine

    def start_car(self) -> str:
        return self.engine.start()
