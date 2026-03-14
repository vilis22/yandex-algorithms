from abc import ABC, abstractmethod


class Plugin(ABC):
    @abstractmethod
    def execute(self, data: str) -> str:
        pass


class UpperCasePlugin(Plugin):
    def execute(self, data: str) -> str:
        return data.upper()


class LowerCasePlugin(Plugin):
    def execute(self, data: str) -> str:
        return data.lower()


def run_plugins(plugins: list[Plugin], data: str) -> list[str]:
    return [plugin.execute(data) for plugin in plugins]
