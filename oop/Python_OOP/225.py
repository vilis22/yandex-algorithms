class Planet:
    def __init__(self, name, time_factor):
        self.name = name
        self.time_factor = time_factor


class Astronaut:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def __get_earth_time(self, days, planet):
        return int(days * planet.time_factor)

    def get_data(self, days, planet):
        return f"{days} дн. на планете {planet.name},\nравно {self.__get_earth_time(days, planet)} дн. на Земле"


plan = Planet("Mars", 1.1)
print(plan.__dict__)
astr = Astronaut("Юра")
print(astr.__dict__)
print(astr.name)
print(astr._Astronaut__get_earth_time(55, plan))
print(astr.get_data(55, plan))
