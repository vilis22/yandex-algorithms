class Thermostat:
    def __init__(self, temp: float) -> None:
        self._temperature = float(temp)

    def get_temperature(self) -> float:
        return self._temperature

    def set_temperature(self, new_temp: float) -> None:
        if isinstance(new_temp, (int, float)) and 0.0 <= new_temp <= 100.0:
            self._temperature = float(new_temp)
