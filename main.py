import random as r
from abc import ABC, abstractmethod
class Hero(ABC):
    @abstractmethod
    def ChangrWeapon(self, weapon):
        pass

class Fighter():
    def __init__(self, name, weapon = None, health = 100):
        self.name = name
        self.weapon = weapon
        self.health = health

    def ChangeWeapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {self.weapon.name}")

    def attack(self, enemy):
       enemy.health -= self.weapon.damage
       print(f"\n{self.name} наносит удар {self.weapon.name}ом {enemy.name}у.\n Здоровье {enemy.name}а = {enemy.health}")

class Monster():
    def __init__(self, name, weapon = None, health = 100):
        self.weapon = weapon
        self.name = name
        self.health = health

    def ChangeWeapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {self.weapon.name}")

    def attack(self, enemy):
        enemy.health -= self.weapon.damage
        print(f"\n{self.name} наносит удар {self.weapon.name}ом {enemy.name}у.\n Здоровье {enemy.name}а = {enemy.health}")

class Weapons(ABC):
    def attack(self):
        pass

class Sword():
    def __init__(self, name, damage = 30):
        self.damage = damage
        self.name = name



class Bow():
    def __init__(self, name, damage = 20):
        self.damage = damage
        self.name = name

def Fight(hero1, hero2):
    while hero1.health > 0 and hero2.health > 0:

        hero1.ChangeWeapon(r.choice(weapon_list))
        hero2.ChangeWeapon(r.choice(weapon_list))

        if r.randint(1, 2) == 1:
            hero1.attack(hero2)
        else:
            hero2.attack(hero1)


    if hero1.health > 0:
        print(f"{hero1.name} победил")
    else:
        print(f"{hero2.name} победил")

hero_list = []
fighter = Fighter("Воин")
monster = Monster("Монстр")
hero_list.append(fighter)
hero_list.append(monster)

weapon_list = []
Topor = Sword("Топор")
Kinet = Bow("Кинжал")
weapon_list.append(Topor)
weapon_list.append(Kinet)

Fight(hero_list[0], hero_list[1])