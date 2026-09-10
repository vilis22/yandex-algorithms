class Flash:
    def __init__(self, capacity=64000):
        self.capacity = capacity
        self.busy_memory = 0
        self.data = []

    def record(self, cd):
        for track in cd:
            if self.capacity - self.busy_memory - track[1] > 0:
                self.busy_memory += track[1]
                self.data.append(track)
            else:
                print("Не хватает памяти для записи!")
                break

        self.show_data()

    def show_data(self):
        print(f"Емкость - {self.capacity}")
        print(f"Занято памяти - {self.busy_memory}")
        print(f"Содержимое - {self.data}\n")


fl = Flash(1)
print(fl.__dict__)
fl = Flash()
print(fl.__dict__)

fl.show_data()
fl.record([("как класть.mp3", 1000), ("морда", 5000), ("красивое.jpg", 7500)])
fl.record(
    [("фотосессия олега на дереве", 10000), ("восстание живых голубцов.mkv", 15000), ("код на бессмертие.txt", 11500)]
)
fl.record(
    [
        ("свадьба олеси и кирилла", 5000),
        ("похороны кирилла.avi", 7000),
        ("рецепт бутерброда из пельменей и изюма.txt", 9000),
    ]
)
fl.record([("Белка угоняет электросамокат!!Ржака!!!.mkv", 5800), ("как замариновать лошадь", 7800)])
