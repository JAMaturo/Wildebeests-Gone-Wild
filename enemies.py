class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0


class Warthog(Enemy):
    def __init__(self):
        super().__init__(name="Warthog", hp=5, damage=1)


class Lion(Enemy):
    def __init__(self):
        super().__init__(name="Lion", hp=25, damage=20)


class Rhinoceros(Enemy):
    def __init__(self):
        super().__init__(name="Rhinoceros", hp=30, damage=15)
