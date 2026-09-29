class Warrior:
    COEFFICIENTS = {0: 1.0, 1: 0.75, 2: 0.50, 3: 0.25}

    def __init__(self, hp, arm=0, m_arm=0):
        self.hp = hp
        self.arm = arm
        self.m_arm = m_arm

    def __setattr__(self, key, value):
        if key in ("arm", "m_arm"):
            if not isinstance(value, int) or value not in self.COEFFICIENTS:
                raise TypeError("Низзяяя!!!")

        super().__setattr__(key, value)

    def _incoming_damage(self, projectile):
        ((typ, dmg),) = projectile.damage.items()
        coefficient = self.COEFFICIENTS[self.arm if typ == "phys" else self.m_arm]
        return dmg * coefficient

    def __lt__(self, other):
        if not isinstance(other, Projectile):
            return NotImplemented

        return self.hp < self._incoming_damage(other)

    def __gt__(self, other):
        if not isinstance(other, Projectile):
            return NotImplemented

        return self.hp > self._incoming_damage(other)


class Projectile:
    DAMAGE_TYPES = ("phys", "magic")

    def __init__(self, typ, damage):
        if typ not in self.DAMAGE_TYPES:
            raise ValueError(f"typ must be one of {self.DAMAGE_TYPES}")

        self.damage = {typ: damage}


war_1 = Warrior(3000)
print(war_1.__dict__)
try:
    war_1.__setattr__("arm", 4.0)
except TypeError as e:
    print(e)
try:
    war_1.__setattr__("m_arm", 5)
except TypeError as e:
    print(e)

pr_1 = Projectile("phys", 1000)
print(pr_1.__dict__)
print(war_1 > pr_1, pr_1 < war_1)

pr_2 = Projectile("magic", 3000)
print(war_1 > pr_2, pr_2 < war_1)
