class Order:
    def __init__(self, order_id, amount):
        self.order_id = order_id
        self.amount = amount

    def __repr__(self):
        return f"Order(order_id={self.order_id!r}, amount={self.amount!r})"

    def __str__(self):
        return f"Заказ №{self.order_id}"
