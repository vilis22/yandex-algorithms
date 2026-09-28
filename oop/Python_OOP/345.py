class Decor:
    @staticmethod
    def cash(func):
        cache = {}

        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))

            if key not in cache:
                cache[key] = func(*args, **kwargs)

            return cache[key]

        return wrapper


class ComplexCalc:
    def calc(self, n):
        return sum(num**3 for num in range(1, n + 1))
