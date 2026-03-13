class Counter:
    total_count = 0

    def __init__(self):
        self.instance_count = 0
        Counter.total_count += 1

    def increment(self):
        self.instance_count += 1

    @classmethod
    def get_total_count(cls):
        return cls.total_count

    @staticmethod
    def get_description():
        return "Это класс для подсчета."
