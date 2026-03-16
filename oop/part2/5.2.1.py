from dataclasses import dataclass


@dataclass(frozen=True)
class Transaction:
    amount: float
    description: str


class AccountError(Exception):
    pass


class TransactionError(AccountError):
    pass


class Account:
    def __init__(self, owner: str, initial_balance: float = 0.0) -> None:
        self.owner = owner
        self._initial_balance = initial_balance
        self._transactions = []

    @property
    def balance(self) -> float:
        return self._initial_balance + sum(t.amount for t in self._transactions)

    def add_transaction(self, transaction: Transaction) -> None:
        if self.balance + transaction.amount < 0:
            raise TransactionError("Транзакция невозможна: недостаточно средств.")
        self._transactions.append(transaction)

    @classmethod
    def from_csv(cls, csv_string: str) -> "Account":
        owner, initial_balance = csv_string.split(",")
        return cls(owner, float(initial_balance))

    def __len__(self) -> int:
        return len(self._transactions)

    def __str__(self) -> str:
        return f"Счет {self.owner}"

    def __repr__(self) -> str:
        return f"Account(owner={self.owner!r}, initial_balance={self._initial_balance!r})"


if __name__ == "__main__":
    acc = Account("Иван", 100)
    acc.add_transaction(Transaction(50, "Пополнение"))
    print(acc.balance)
    print(len(acc))
    acc.add_transaction(Transaction(-200, "Покупка"))
