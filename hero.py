#hero.py
import random
from ability import Ability
from armor import Armor
from weapon import Weapon


class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()
        self.deaths = 0
        self.kills = 0

    
    def add_kill(self, num_kills):
        ''' Update self.kills by num_kills amount'''
        self.kills += num_kills
        
    def add_death(self, num_deaths):
        ''' Update deaths with num_deaths'''
        self.deaths += num_deaths

    def fight (self, opponent):
        """Current Hero will take turns fighting the opponent hero passed in"""
        all_my_heroes {}
        for h in opponent:
            all_my_heroes[h] = all_my_heroes.get(h,0)+1
        for key in all_my_heroes.keys():
            if key == False
            print ('Draw')
         # 1) the number of kills the hero (self) has when the opponent dies.
        # 2) then number of kills the opponent has when the hero (self) dies
        # 3) the number of deaths of the opponent if they die    in the fight
        # 4) the number of deaths of the hero (self) if they die in the fight
    

    def add_ability(self, ability):
        """Add ablity to abilities list"""
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)
         

    def attack(self):
        """calculate the total damage from all anility attcks. return: total_damage:Int"""
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
            return total_damage

    def add_armor(self, armor):
        """ Add armor to self.armors Armor: Armor Object"""
        total_protection = 0
        for armor in self.armors:
            total_protection += armor.add_armor()
            return total_protection

    def defend(self, damage_amt):
        """Calc total block amount from all armour blocks."""
    pass
        # for armor in self.armors:
        #     total_block += armor.block()
        #     return total_block 

    def take_damage(self, damage):
        """Updates self.current_health to reflect the damage minus the defense."""
        # self.current_health -= self.defend(damage)
        # return self.current_health
    pass

    def is_alive(self):
        """Return True or False depending on whether the hero is alive or not."""
        # if self.current_health <= 0:
        #      False
        # else:
        #      True

    pass
   


if __name__=='__main__':
    # my_hero = Hero('Grace Hopper', 200)
    # print(my_hero.name)
    # print(my_hero.current_health) 
    # #hero1 = Hero('Wonder Woman')
    # #hero2 = Hero('Dumbledore')
    # #hero1.fight(hero2)
    # ability = Ability("Great Debugging", 50)
    # another_ability = Ability("Smarty Pants", 90)
    # hero = Hero("Grace Hopper", 200)
    # hero.add_ability(ability)
    # hero.add_ability(another_ability)
    # print(hero.attack())
    # hero = Hero("Grace Hopper", 200)
    # shield = Armor("Shield", 50)
    # hero.add_armor(shield)
    # hero.take_damage(50)
    # print(hero.current_health)
    # hero = Hero("Grace Hopper", 200)
    # hero.take_damage(150)
    # print(hero.is_alive())
    # hero.take_damage(15000)
    # print(hero.is_alive())
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())


  