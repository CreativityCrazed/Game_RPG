from Player import *

class Characteristic:
    chars = {"strength" : 8, "dexterity" : 8, "physique" : 8, "intelligence" : 8, "wisdom" : 8, "charisma" : 8}
    mods = {"strength" : 0, "dexterity" : 0, "physique" : 0, "intelligence" : 0, "wisdom" : 0, "charisma" : 0}
    strength = 8
    dexterity = 8
    physique = 8
    intelligence = 8
    wisdom = 8
    charisma = 8
    mod = 0

    def Mod(self):
        for char, value in self.chars.items():
            if value <= 1:
                self.mods[char] = -5
            elif value <= 3:
                self.mods[char] = -4
            elif value <=  5:
                self.mods[char] = -3
            elif value <=  7:
                self.mods[char] = -2
            elif value <=  9:
                self.mods[char] = -1
            elif value <=  11:
                self.mods[char] = 0
            elif value <=  13:
                self.mods[char] = +1
            elif value <=  15:
                self.mods[char] = +2
            elif value <=  17:
                self.mods[char] = +3
            elif value <=  19:
                self.mods[char] = +4
            elif value <=  21:
                self.mods[char] = +5

    def Physique(self):
        self.Mod(self.physique)
        Player.hp += self.Mod(self.physique)
