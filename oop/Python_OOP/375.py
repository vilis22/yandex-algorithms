class StoreError(Exception):
    def __init__(self, missing: list | None = None, out_of_stock: list | None = None) -> None:
        self.missing = missing or []
        self.out_of_stock = out_of_stock or []
        super().__init__(self._format_message())

    def _format_message(self) -> str:
        if self.missing:
            msg = f'Продуктов нет в базе - "{", ".join(self.missing)}"'
            if self.out_of_stock:
                msg += f'\nТакже не хватает - "{", ".join(self.out_of_stock)}"'

            return msg

        if self.out_of_stock:
            return f'Не хватает - "{", ".join(self.out_of_stock)}"'

        return ""


class Error1(StoreError):
    pass


class Error2(StoreError):
    pass


class Error3(StoreError):
    pass


class Store:
    def __init__(self, goods: dict[str, list[int]]) -> None:
        self.goods = {name: [quantity, price] for name, (quantity, price) in goods.items()}
        self.sum = self._calculate_total()

    def _calculate_total(self) -> int:
        return sum(quantity * price for quantity, price in self.goods.values())

    def sall(self, **orders: int) -> None:
        missing = []
        out_of_stock = []

        for item, count in orders.items():
            if item not in self.goods:
                missing.append(item)
                continue

            stock, _ = self.goods[item]

            if stock < count:
                out_of_stock.append(f"{item} - {count - stock}")
                continue

        if missing and out_of_stock:
            raise Error1(missing=missing, out_of_stock=out_of_stock)

        if missing:
            raise Error2(missing=missing)

        if out_of_stock:
            raise Error3(out_of_stock=out_of_stock)

        for item, count in orders.items():
            self.goods[item][0] -= count

            if self.goods[item][0] == 0:
                del self.goods[item]

        self.sum = self._calculate_total()

    def __bool__(self):
        return self.sum != 0


if __name__ == "__main__":
    st = Store({"макароны": [5, 150], "затылок": [3, 1200], "кукарача": [12, 500], "горбуша": [6, 2000]})
    print(st.__dict__)
    st.sall(
        макароны=2,
        кукарача=4,
    )
    print(st.__dict__)
    try:
        st.sall(пудра=6, выдра=6, горбуша=7)
    except (Error1, Error2, Error3) as e:
        print(e)
    print(st.__dict__)
    try:
        st.sall(майонезный_чак_чак=7, собачья_икра=22)
    except (Error1, Error2, Error3) as e:
        print(e)
    print(st.__dict__)
    try:
        st.sall(горбуша=7, кукарача=22, затылок=11)
    except (Error1, Error2, Error3) as e:
        print(e)
    print(st.__dict__)
    print(bool(st))
    st.sall(горбуша=6, кукарача=8, затылок=3, макароны=3)
    print(st.__dict__)
    print(bool(st))
