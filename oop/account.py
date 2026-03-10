from decimal import Decimal


class Account:
    def __init__(self, balance: Decimal) -> None:
        self._balance = balance

    def get_balance(self) -> Decimal:
        return self._balance
