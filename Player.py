import random
from Inventory import *

class Player:
    name: str
    max_hp = 10
    hp = max_hp
    min_dmg = 2
    max_dmg = 5
    lvl = 1
    max_lvl = 5
    exp = 0
    lvlup = [0, 5, 10, 20, 50]
    gold = 0
    is_death = False
    inventory = Inventory()

# Создаёт имя перса
    def __init__(self, name):
        self.name = name
# Восскрешение
    def heal(self):
        self.hp = self.max_hp
        self.is_death = False
# Рандомит урон
    def get_dmg(self):
        return random.randint(self.min_dmg, self.max_dmg)

# Выводи на экран сообщение о статусе персонажа
    def print_stats(self):
        print(self.name, f"""
Уровень: {self.lvl}
Опыт: {self.exp}
Золото: {self.gold}
Жизни: {self.hp}
Урон: {self.min_dmg} - {self.max_dmg}
""")

    def print_items(self):
        self.inventory.print_items()

# Урон от моба
    def set_dmg(self, dmg):
        print(f"Игроку нанесли урон: {dmg}")
        self.hp -= dmg
        if self.hp <= 0:
            self.hp = 0
            self.death()

# Проверка жив ли игрок
    def death(self):
        print("Чувак, ты помер)")
        self.is_death = True
# Выдаёт голду
    def add_gold(self, gold):
        self.gold += gold
        print(f"Вы получили золото: {gold}")
# Выдаёт экспу
    def add_exp(self, exp):
        self.exp += exp
        if self.lvl < self.max_lvl:
            exp_lvlup = self.lvlup[self.lvl]
            print(f"Вы получили опыт: {exp}")
            if self.exp >= exp_lvlup:
                self.lvl += 1
                self.max_hp += 2
                self.min_dmg += 1
                self.max_dmg += 1
                print(f"Вы получили уровень {self.lvl}")
                print("Теперь ваши характеристики такие:")
                self.print_stats()
# Инициализация боя
    def fight(self, monster, is_player_fight=True, is_monster_fight=True):
        if is_player_fight:
            player_dmg = self.get_dmg()
            monster.set_dmg(player_dmg)
            if monster.hp > 0:
                print(f"Жизней осталось у монстра {monster.hp}")
        if is_monster_fight:
            monster_dmg = monster.get_dmg()
            self.set_dmg(monster_dmg)
            print(f"У вас осталось жизней: {self.hp}")
            if monster.is_death:
                exp = monster.get_exp()
                gold = monster.get_gold()
                self.add_gold(gold)
                self.add_exp(exp)

    def add_rand_item(self):
        self.inventory.add_random_item()