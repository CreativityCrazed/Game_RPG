import random

def create_item():
    Items = ["Weapon", "Armor", "Jewel"]
    item_name = random.choice(Items)
    return eval(f"{item_name}()")

class Item:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def print(self):
        print(f"name: {self.name}")
        print(f"type: {self.type}")

class Weapon(Item):
    def __init__(self):
        type = "оружие"
        name = random.choice(["меч", "пика", "лук", "кинжал", "булова", "кастеты", "двуручный меч", "арбалет"])
        Item.__init__(self, name, type)

class Armor(Item):
    def __init__(self):
        type = "броня"
        name = random.choice(["шлем", "доспех", "перчатки", "штаны", "ботинки", "пояс", "щит"])
        Item.__init__(self, name, type)

class Jewel(Item):
    def __init__(self):
        type = "бижа"
        name = random.choice(["амулет", "кольцо", 'браслет'])
        Item.__init__(self, name, type)



