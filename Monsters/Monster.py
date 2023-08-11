import random

class Monster:
    mob = ["skeleton", "spirit"]
    name = mob[random.randint(0, len(mob)-1)]
    lvl = random.randint(1, 3)
    hp = 0
    dmg_mob_min = 0
    dmg_mob_max = 0
    gold_mob = 0
    exp_mob = 0
    is_death = False

# Рандомин мобов
    def __init__(self):
        pass

# Рандомит опыт
    def get_exp(self):
        return self.exp_mob

# Рандомит голду
    def get_gold(self):
        return self.gold_mob


# Выводи на экран сообщение о статусе моба
    def print_stats(self):
        print(self.name, f"""
Уровень: {self.lvl}
Жизни: {self.hp}
Урон: {self.dmg_mob_min} - {self.dmg_mob_max}
""")

# Бой
    def get_dmg(self):
        return random.randint(self.dmg_mob_min, self.dmg_mob_max)

    def set_dmg(self, dmg):
        print(f"Вы нанесли урон: {dmg}")
        self.hp -= dmg
        if self.hp <= 0:
            self.hp = 0
            self.death()

# Проверка на смерть монстра
    def death(self):
        print("Монстр помер)")
        self.is_death = True
