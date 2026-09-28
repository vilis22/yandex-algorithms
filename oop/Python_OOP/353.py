class JetPack:
    def __init__(self, weight_lim: int, bat_cap: int, charge_perc: int) -> None:
        self.weight_lim = weight_lim
        self.bat_cap = bat_cap
        self.charge_perc = charge_perc

    def __str__(self) -> str:
        minutes, seconds = self._get_flight_time()
        return f"{minutes:02d}:{seconds:02d}"

    def _give_me_bal(self) -> int:
        minutes, _ = self._get_flight_time()
        return (self.weight_lim // 10) * 2 + minutes * 3

    def _get_flight_time(self) -> tuple[int, int]:
        free_bat_cap = self.bat_cap * self.charge_perc // 100
        minutes = free_bat_cap // 3000
        seconds = free_bat_cap % 3000 * 60 // 3000
        return minutes, seconds

    def __eq__(self, other: "JetPack") -> bool:
        return self._give_me_bal() == other._give_me_bal()

    def __lt__(self, other: "JetPack") -> bool:
        return self._give_me_bal() < other._give_me_bal()

    def __le__(self, other: "JetPack") -> bool:
        return self._give_me_bal() <= other._give_me_bal()
