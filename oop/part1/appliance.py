class Appliance:
    def __init__(self, model):
        self.model = model
        self.is_on = False

    def turn_on(self):
        self.is_on = True


class Toaster(Appliance):
    pass
