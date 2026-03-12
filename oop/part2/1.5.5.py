class Converter:
    def __init__(self):
        self._meters = 0

    @property
    def meters(self):
        return self._meters

    @meters.setter
    def meters(self, value):
        self._meters = value

    @property
    def kilometers(self):
        return self._meters / 1000

    @kilometers.setter
    def kilometers(self, value):
        self._meters = value * 1000
