class Fish:
    def move(self):
        return "Я плыву"


class Bird:
    def move(self):
        return "Я лечу"


def make_it_move(creature):
    return creature.move()
