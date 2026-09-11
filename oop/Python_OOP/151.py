class File:
    def __init__(self, name: str):
        self.name = name
        self.rights = "user"

    def file_infection(self):
        self.rights = "admin"


class Antivirus:
    quarantine = []

    @classmethod
    def file_check(cls, file: File):
        if file.rights == "admin":
            cls.quarantine.append(file)
            print(f"Файл {file.name} заражен.")
            print("Он отправлен в карантин.")
        else:
            print(f"Файл {file.name} не заражен.")
