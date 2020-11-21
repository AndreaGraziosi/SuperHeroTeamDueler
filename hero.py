#hero.py
import random
from ability import Ability
from armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()

    
    
    def fight (self, opponent):
        """Current Hero will take turns fighting the opponent hero passed in"""
    pass

        #print(f'({random.choice()}"Won!")')

    def add_ability(self, ability):
        """Add ablity to abilities list"""
        self.abilities.append(ability)
         

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
    
        for armor in self.armors:
            total_block += armor.block()
            return total_block 

    def take_damage(self, damage):
        """Updates self.current_health to reflect the damage minus the defense."""
        self.current_health -= self.defend(damage)
        return self.current_health
        

    def is_alive(self):
        """Return True or False depending on whether the hero is alive or not."""
        if self.current_health <= 0:
             False
        else:
             True

        



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
    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())


   