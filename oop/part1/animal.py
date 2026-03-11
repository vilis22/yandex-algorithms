class Animal:
    pass


class Cat(Animal):
    pass


class Dog(Animal):
    pass


def is_pet(animal_object):
    return isinstance(animal_object, (Cat, Dog))
