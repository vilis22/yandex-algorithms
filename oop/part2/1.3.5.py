class Transaction:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __repr__(self):
        return f"Transaction(amount={self.amount!r}, currency={self.currency!r})"

    def __str__(self):
        return f"Транзакция на сумму {self.amount:.2f} {self.currency}"
