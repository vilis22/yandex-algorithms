class Gestures:
    def __init__(self, gest):
        if gest in ["камень", "ножницы", "бумага"]:
            self.gest = gest
        else:
            print("Необходимо выбрать что-то из ['камень', 'ножницы', 'бумага']")


class Game:
    def play(self, gestures1: Gestures, gestures2: Gestures):
        if gestures1.gest == gestures2.gest:
            print("Ничья")
        elif gestures1.gest in ["камень", "ножницы"] and gestures2.gest in ["камень", "ножницы"]:
            print("камень сильнее ножницы")
        elif gestures1.gest in ["ножницы", "бумага"] and gestures2.gest in ["ножницы", "бумага"]:
            print("ножницы сильнее бумага")
        else:
            print("бумага сильнее камень")


gest_1, gest_2 = Gestures("камень"), Gestures("ножницы")
Game().play(gest_1, gest_2)

gest_1, gest_2 = Gestures("бумага"), Gestures("бумага")
Game().play(gest_1, gest_2)

gest_1, gest_2 = Gestures("ножницы"), Gestures("камень")
Game().play(gest_1, gest_2)

gest_1, gest_2 = Gestures("бумага"), Gestures("камень")
Game().play(gest_1, gest_2)

gest_1, gest_2 = Gestures("камень"), Gestures("бумага")
Game().play(gest_1, gest_2)

# gest_1 = Gestures("бумаг")
