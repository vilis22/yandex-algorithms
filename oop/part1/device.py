class Device:
    def __init__(self) -> None:
        self._voltage: int = 0

    def get_voltage(self) -> int:
        return self._voltage

    def set_voltage(self, new_voltage: int) -> None:
        self._voltage = new_voltage
