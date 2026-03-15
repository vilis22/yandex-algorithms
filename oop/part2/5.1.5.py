class AtmError(Exception):
    pass


class InsufficientFundsError(AtmError):
    pass


class InvalidPinError(AtmError):
    pass


class ATM:
    def __init__(self, balance, pin):
        self.balance = balance
        self.pin = pin

    def withdraw(self, amount, entered_pin):
        if entered_pin != self.pin:
            raise InvalidPinError()

        if amount > self.balance:
            raise InsufficientFundsError()

        self.balance -= amount
        return self.balance
