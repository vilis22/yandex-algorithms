from decimal import Decimal


class BankAccount:
    def __init__(self, balance: Decimal):
        self._balance = balance
