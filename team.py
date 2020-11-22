#team.py
import random

class Team:
    def __init__(self, name):
        self.name = name 
        self.heroes = list()

    def add_hero(self, name):
        self.heroes.append(name)
    
    def remove_hero(self, name):
        '''Remove hero from heroes list. If Hero isn't found return 0.'''
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
                return 0
    
    def view_all_heroes(self):
        """Prints all heroes to the console"""
        for hero in self.heroes:
            print (hero)

    def stats(self):
        '''Print team statistics'''
    for hero in self.heroes:
        kd = hero.kills / hero.deaths
        print("{} Kill/Deaths:{}".format(hero.name,kd))

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        for hero in self.hero:
            self.current_health = self.starting_health

    def attack(self, other_team):
        ''' Battle each team against each other.'''
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents)> 0:
             living = random.choice(living_heroes)
            self.name.fight(self.name)
            living_heroes, living_opponents.append(self.name)

