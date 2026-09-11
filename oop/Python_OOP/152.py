class Robot:
    pass


class Human:
    pass


class Examination:
    @staticmethod
    def identification(obj):
        return isinstance(obj, Robot)


hum, rob = Human(), Robot()
print(Examination.identification(rob))
print(Examination.identification(hum))
