class Car:
    total_cars: int = 0

    def __init__(self, brand: str, model: str) -> None:
        self.brand = brand
        self.model = model
        type(self).total_cars += 1

    @classmethod
    def get_total_cars(cls) -> int:
        return cls.total_cars
