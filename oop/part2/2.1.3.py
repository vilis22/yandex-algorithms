from decimal import Decimal


class Product:
    def __init__(self, name: str, price: Decimal) -> None:
        self.name = name
        self.price = price

    @classmethod
    def from_dict(cls, product_dict: dict) -> "Product":
        name = product_dict.get("name", "Unknown Product")
        price = Decimal(str(product_dict.get("price", 0)))
        return cls(name, price)
