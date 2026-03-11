class Character:
    def __init__(self, name, damage):
        self.name = name
        self._health = 100
        self._damage = damage

    def attack(self, target):
        if hasattr(target, "take_damage") and callable(target.take_damage):
            target.take_damage(self._damage)

    def take_damage(self, amount):
        self._health -= amount

    def get_status(self):
        return f"Имя: {self.name}, Здоровье: {self._health}"


class Warrior(Character):
    def __init__(self, name, damage, armor):
        super().__init__(name, damage)
        self.armor = armor

    def take_damage(self, amount):
        actual_damage = max(0, amount - self.armor)
        self._health -= actual_damage


class Mage(Character):
    def __init__(self, name, damage, mana):
        super().__init__(name, damage)
        self.mana = mana

    def attack(self, target):
        if self.mana >= 10:
            self.mana -= 10
            super().attack(target)


if __name__ == "__main__":
    # Создаем персонажей
    warrior = Warrior("Конан", 15, 5)  # Урон 15, Броня 5
    mage = Mage("Раистлин", 20, 100)  # Урон 20, Мана 100

    print(warrior.get_status())
    print(mage.get_status())
    print("--- Битва ---")

    # Маг атакует воина
    mage.attack(warrior)
    print(warrior.get_status())  # Воин должен получить 15 урона (20 - 5 брони)

    # Воин атакует мага
    warrior.attack(mage)
    print(mage.get_status())  # Маг должен получить 15 урона

    # Проверка логики мага
    mage.mana = 5  # Устанавливаем мало маны
    mage.attack(warrior)
    print(warrior.get_status())  # Здоровье воина не должно измениться
