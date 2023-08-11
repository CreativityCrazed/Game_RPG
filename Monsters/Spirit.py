from Monsters.Monster import *

class Spirit(Monster):

    def __init__(self):

        self.name == "Spirit"

        if self.lvl == 1:
            self.hp = random.randint(2, 4)
            self.dmg_mob_min = random.randint(1, 3)
            self.dmg_mob_max = random.randint(3, 4)
            self.gold_mob = random.randint(3, 4)
            self.exp_mob = random.randint(1, 3)
        if self.lvl == 2:
            self.hp  = random.randint(3, 5)
            self.dmg_mob_min = random.randint(2, 3)
            self.dmg_mob_max = random.randint(3, 5)
            self.gold_mob = random.randint(3, 5)
            self.exp_mob = random.randint(2, 3)
        if self.lvl == 3:
            self.hp = random.randint(4, 7)
            self.dmg_mob_min = random.randint(2, 3)
            self.dmg_mob_max = random.randint(4, 5)
            self.gold_mob = random.randint(4, 5)
            self.exp_mob = random.randint(2, 3)
