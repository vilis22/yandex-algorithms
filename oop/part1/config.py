class Config:
    theme = "light"

    def __init__(self, app_name: str):
        self.app_name = app_name

    def get_theme(self) -> str:
        return self.theme
