class PC:
    def __init__(self, lst, access=False):
        self.access = access
        self.__lst = [hash(pas) for pas in lst]

    def valid_psw(self, psw):
        if hash(psw) in self.__lst:
            self.access = True
            return

        raise TypeError("Низзяяя!!!")


pc = PC(["123456", "пороль", "дюшес", "овощебаза", "fdr%$^%fGJYJK##)W@"])
print(*pc.__dict__, pc.access)

print(all([hash(i) in pc._PC__lst for i in ["123456", "пороль", "дюшес", "овощебаза", "fdr%$^%fGJYJK##)W@"]]))

try:
    pc.valid_psw("пароль")
except TypeError as e:
    print(e)
print(*pc.__dict__, pc.access)

pc.valid_psw("овощебаза")
print(*pc.__dict__, pc.access)
