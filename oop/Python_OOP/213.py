class Reincarnation:
    __prev = None

    def __init__(self, life_form):
        self.life_form = life_form
        self.prev = Reincarnation.__prev
        Reincarnation.next_prev(self)

    @classmethod
    def next_prev(cls, obj):
        cls.__prev = obj


print(Reincarnation._Reincarnation__prev)

reincar_1 = Reincarnation("Бубузяна")
print(reincar_1.prev, reincar_1.life_form)
#
reincar_2 = Reincarnation("одноногий комар Валера")
print(reincar_2.prev.life_form, reincar_2.life_form)
#
reincar_3 = Reincarnation("Енотовидная бабайка")
print(reincar_3.prev.life_form, reincar_3.life_form)
#
print(Reincarnation.next_prev)
