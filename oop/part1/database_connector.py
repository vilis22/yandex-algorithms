class DatabaseConnector:
    def __init__(self) -> None:
        self.is_connected = False

    def _establish_connection(self) -> None:
        self.is_connected = True

    def connect(self) -> None:
        self._establish_connection()
