class Config:
    def __init__(self):
        self._port = 80

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, new_port):
        try:
            self._port = int(new_port)
        except ValueError:
            pass


if __name__ == "__main__":
    port = Config()
    port.port = "30"
    print(port.port)
