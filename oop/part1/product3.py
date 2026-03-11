class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class DiscountedProduct(Product):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def get_price_with_discount(self):
        return self.price - self.price * self.discount / 100
