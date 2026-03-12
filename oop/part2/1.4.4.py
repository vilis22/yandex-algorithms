class Grades:
    def __init__(self):
        self._grades = {"math": 5, "history": 4}

    def __getitem__(self, item):
        return self._grades[item]
