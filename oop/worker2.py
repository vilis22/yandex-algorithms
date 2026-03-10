class Worker:
    def __init__(self, name, position):
        self._name = name
        self._position = position

    @property
    def name(self):
        return self._name

    @property
    def position(self):
        return self._position


class HRManager(Worker):
    def get_employee_info(self):
        return f"Имя: {self.name}, Должность: {self.position}"
