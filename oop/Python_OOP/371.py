class Mine:
    def __init__(self, mine):
        self.mine = mine

    def __len__(self):
        return sum(int(count) for item in self.mine if (parts := item.split())[0] == "титрил" and (count := parts[1]))

    def __bool__(self):
        return bool(len(self))


mine_1 = Mine(["халва 7", "агуша 9", "титан 4"])
print(mine_1.__dict__.values())
print(len(mine_1))
print(bool(mine_1))

mine_2 = Mine(["мякиш 12", "песок 2", "титрил 7", "шерсть 22"])
print(mine_2.__dict__.values())
print(len(mine_2))
print(bool(mine_2))

mine_3 = Mine(["титрил 15", "щавель 6", "бобрюминий 22", "титрил 17", "пенопластокваша 55"])
print(mine_3.__dict__.values())
print(len(mine_3))
print(bool(mine_3))
