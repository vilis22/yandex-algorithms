from abc import ABC, abstractmethod
from datetime import datetime


class Handler(ABC):
    @abstractmethod
    def emit(self, message: str) -> str | None:
        pass


class ConsoleHandler(Handler):
    def emit(self, message: str) -> None:
        print(message)


class FileHandler(Handler):
    def emit(self, message: str) -> str:
        return f"Запись в файл: {message}"


class TimeMixin:
    def format_with_timestamp(self, message: str) -> str:
        return f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{message}]"


class Logger(TimeMixin):
    def __init__(self, handlers: list[Handler]) -> None:
        self._handlers = handlers

    def log(self, message: str) -> None:
        formatted_message = self.format_with_timestamp(message)

        for handler in self._handlers:
            handler.emit(formatted_message)

    def __call__(self, *args, **kwargs) -> None:
        return self.log(*args, **kwargs)
