class Generator:
    def gen_numbers(self, n=1):
        while True:
            yield n
            n += 1

    def __str__(self):
        return "Я экземпляр класса Generator и могу создать генератор))"
