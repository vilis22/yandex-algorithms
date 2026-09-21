class Hunter:
    def __init__(self):
        self._dct = {}
        self._hp = 15000

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp -= value

    @property
    def dct(self):
        return self._dct

    @dct.setter
    def dct(self, value):
        item, radiation, seconds = value

        self._dct[item] = self._dct.get(item, 0) + radiation

        total_radiation = sum(self._dct.values())
        self.hp = total_radiation * seconds

    def __len__(self):
        return sum(self._dct.values())
