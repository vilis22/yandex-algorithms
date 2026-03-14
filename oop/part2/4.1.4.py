from abc import ABC, abstractmethod


class Instrument(ABC):
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        return f"Бренд: {self.brand}"

    @abstractmethod
    def play(self):
        pass


class Guitar(Instrument):
    def play(self):
        return "Играет мелодия на гитаре"
