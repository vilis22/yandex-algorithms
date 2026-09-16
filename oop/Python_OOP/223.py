from math import gcd


class AspectRatio:
    def __init__(self, resolution):
        self.ar = resolution

    @property
    def ar(self):
        return self.__ar

    @ar.setter
    def ar(self, resolution):
        w, h = map(int, resolution.split())

        if w < h:
            w, h = h, w

        g = gcd(w, h)
        self.__ar = f"{w // g}:{h // g}"


x = AspectRatio("1920 1080")
print(x.__dict__)
print(x.ar)

x = AspectRatio("640 480")
print(x.__dict__)
print(x.ar)

x = AspectRatio("480 640")
print(x.__dict__)
print(x.ar)

x = AspectRatio("555 76")
print(x.__dict__)
print(x.ar)

x = AspectRatio("75 555")
print(x.__dict__)
print(x.ar)

x = AspectRatio("3840 2160")
print(x.__dict__)
print(x.ar)
