class Descriptor:
    def __get__(self, instance, owner):
        print("Я родился")


class Luntik:
    desc = Descriptor()

    def __init__(self):
        _ = self.desc


lnt = Luntik()
