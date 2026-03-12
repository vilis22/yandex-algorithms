class Player:
    def __init__(self, nickname, level):
        self.nickname = nickname
        self.level = level

    def __repr__(self):
        return f"Player(nickname={self.nickname!r}, level={self.level!r})"
