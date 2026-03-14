from abc import ABC, abstractmethod


class DataSource(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass


class FileStorage(DataSource):
    def read(self):
        return "Чтение из файла"

    def write(self, data):
        return f"Запись в файл: {data}"
