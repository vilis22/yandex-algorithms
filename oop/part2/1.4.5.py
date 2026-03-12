class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __lt__(self, other):
        return self.price < other.price

    def __repr__(self):
        return f"Item({self.name!r}, {self.price!r})"
