class Crocodile:
    def __init__(self, mood):
        self.__mood = mood

    @property
    def mood(self):
        return self.__mood

    def do_a_trick(self):
        if self.__mood == "добрый":
            print("Можно")
        elif self.__mood == "злой":
            print("можно, но в последний раз")


cr = Crocodile("злой")
print(cr.mood)
print(cr.__dict__)
cr.do_a_trick()
cr._Crocodile__mood = "добрый"
print(cr.mood)
print(cr.__dict__)
cr.do_a_trick()
