class Radio:
    def play(self):
        return "Радио играет"


class Speaker:
    def play(self):
        return "Колонка играет"


class Boombox(Radio, Speaker):
    pass


if __name__ == "__main__":
    boom = Boombox()
    print(boom.play())
