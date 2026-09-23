class Mutagen:
    def __setattr__(self, key, value):
        if key == "lst" and isinstance(value, list):
            value = [word for word in value if "мутаген" in word]
        object.__setattr__(self, key, value)

    def get_data(self, file_path="borch_s_kapustkoi.txt"):
        with open(file_path, encoding="utf-8") as file:
            return [w.strip() for w in file.read().split(",") if w.strip()]


mutagen = Mutagen()
print(mutagen.get_data())

mutagen.lst = mutagen.get_data()
print(mutagen.lst)

mutagen.lst = ["уроборос", "старс", "вкусно чешется"]
print(mutagen.lst)

mutagen.lst = "маленько укулеле сделал"
print(mutagen.lst)

mutagen.__setattr__("lst", mutagen.get_data())
print(mutagen.lst)
