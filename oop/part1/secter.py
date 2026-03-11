class Secret:
    def __init__(self, secret_message: str):
        self._message = secret_message

    def get_message(self) -> str:
        return self._message
