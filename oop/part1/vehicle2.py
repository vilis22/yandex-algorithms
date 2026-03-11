class Vehicle:
    pass


class Car(Vehicle):
    pass


class Boat(Vehicle):
    pass


def is_land_vehicle(vehicle_class):
    return issubclass(vehicle_class, Car)
