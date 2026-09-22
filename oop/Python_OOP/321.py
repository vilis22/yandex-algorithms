class Mirror:
    def __init__(self, age):
        self.reflection = age

    def __getattribute__(self, item):
        return int(object.__getattribute__(self, item) / 100 * 80)


mir = Mirror(73)
print(mir.reflection)
