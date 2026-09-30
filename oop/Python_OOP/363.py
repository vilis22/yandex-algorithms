class Cards:
    weights = {"6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "валет": 11, "дама": 12, "король": 13, "туз": 14}

    def __init__(self, lst, trump):
        self.trump = trump
        self.lst = lst

    def get_weight(self, card):
        card_split = card.split()

        if card_split[1] == self.trump:
            return self.weights[card_split[0]] + 9

        return self.weights[card_split[0]]

    def sort(self):
        self.lst = sorted(self.lst, key=self.get_weight)

    def __hash__(self):
        return hash(sum(self.get_weight(card) for card in self.lst))


cards_1 = Cards(["6 к", "дама б", "король ч", "туз в", "6 ч", "дама в", "король б", "туз к"], "ч")
print(cards_1.__dict__)
cards_1.sort()
print(cards_1.lst)

cards_2 = Cards(["дама б", "6 к", "6 ч", "туз в", "король б", "туз к", "дама в", "король ч"], "ч")
cards_2.sort()
print(cards_2.lst)
print(hash(cards_1) == hash(cards_2))

cards_3 = Cards(["7 б", "валет в", "туз к", "король б", "9 ч"], "в")
cards_4 = Cards(["король к", "10 ч", "8 б", "дама в", "валет ч"], "к")
cards_3.sort(), cards_4.sort()
print(cards_3.lst)
print(cards_4.lst)
print(hash(cards_3) == hash(cards_4))

cards_5 = Cards(["9 б", "10 б", "дама в", "7 к", "валет ч"], "б")
cards_6 = Cards(["10 б", "9 б", "7 к", "король ч", "дама в"], "б")
cards_5.sort(), cards_6.sort()
print(cards_5.lst)
print(cards_6.lst)
print(hash(cards_5) == hash(cards_6))
