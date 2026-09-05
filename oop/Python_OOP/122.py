class TumbaUmba:
    pass


def func(n: int) -> list[TumbaUmba]:
    clan = []

    for i in range(1, n + 1):
        person = TumbaUmba()

        if i % 3:
            person.warrior = True
        else:
            person.warrior = False

        clan.append(person)

    return clan
