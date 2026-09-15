class ShopingList:
    def __init__(self, lst=None):
        self.__lst = list(lst) if lst else []

    def add_list(self, obj):
        self.__lst.append(obj)

    @property
    def lst(self):
        return self.__lst

    @lst.setter
    def lst(self, item):
        self.__lst = item


sp = ShopingList(["крем чиз", "бизе", "хруст молока", "кашица из оттуда"])
print(sp.__dict__)
print(sp.lst)
sp.add_list("куропатыч")
print(sp.lst)
sp.add_list("баклажаба")
print(sp.lst)
sp = ShopingList()
print(sp.__dict__)
print(sp.lst)
sp.lst = ["кошачий хавчик", "кость стрекозы", "влажный сахар", 'пельмени "Трешачок"']
print(sp.lst)
