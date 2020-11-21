#hero.py
import random

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    
   
    def fight (self, opponent):
        """Current Hero will take turns fighting the opponent hero passed in"""
        #print(f'({random.choice()}"Won!")')

my_hero = Hero('Grace Hopper', 200)
print(my_hero.name)
print(my_hero.current_health)       

hero1 = Hero('Wonder Woman')
hero2 = Hero('dumbledore')




if __name__=='__main__':
    hero1 = Hero('Wonder Woman')
    hero2 = Hero('Dumbledore')

hero1.fight(hero2) 
   