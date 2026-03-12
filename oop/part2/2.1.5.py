class Website:
    @classmethod
    def get_description(cls) -> str:
        return "Это общий сайт."


class Shop(Website):
    @classmethod
    def get_description(cls) -> str:
        return "Это интернет-магазин."
