class AppSettings:
    def __init__(self, user_id: int, theme: str):
        self.user_id = user_id
        self._theme = theme
