class Validator:
    @staticmethod
    def is_positive(number):
        return number > 0

    @staticmethod
    def is_even(number):
        return not number % 2
