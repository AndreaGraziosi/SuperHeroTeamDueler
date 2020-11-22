from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        def __init__(self, team_one, team_two):
            self.team_one = team_one
            self.team_two = team_two

        def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        name = input("What is the ability name?  ")
        max_damage = input(
            "What is the max damage of the ability?  ")

        return Ability(name, max_damage)

        def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        weapon_name = input("what is the name of your weapon")
        weapon_description = input("What does this weapon do?")
        return Weapon(weapon_name, weapon_description)

        def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''

          armor_name = input("what piesce of armor do you want")
          armor_specs = input("what materails do you need")
          return Armor(armor,armor_specs)

        def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None

        while add_item != "4":
           add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
           if add_item == "1":
               ability = self.create_ability()
               hero.create_ability()
               
           elif add_item == "2":
               weapon = self.create_weapon()
               hero.create_weapon()
           elif add_item == "3":
               armor = self.create_armor()
               hero.create_armor()
        return hero

           
    def build_team_one(self):
        '''Prompt the user to build team_one '''
        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)
            
    
    def build_team_two(self):
        '''Prompt the user to build team_two'''
        numOfTeamMembers2 = int(input("How many members would you like on Team two?\n"))
        for i in range(numOfTeamMembers2):
            hero = self.create_hero()
            self.team_two.add_hero(hero)
  
    def team_battle(self):
        '''Battle team_one and team_two together.'''
        team_one.attack(team_two)

    def show_stats(self):
        '''Prints team statistics to terminal.'''

        print("\n")
    print(self.team_one.name + " statistics: ")
    self.team_one.stats()
    print("\n")
    print(self.team_two.name + " statistics: ")
    self.team_two.stats()
    print("\n")

    # This is how to calculate the average K/D for Team One
    team_kills = 0
    team_deaths = 0
    for hero in self.team_one.heroes:
        team_kills += hero.kills
        team_deaths += hero.deaths
    if team_deaths == 0:
        team_deaths = 1
    print(self.team_one.name + " average K/D was: " + str(team_kills/team_deaths))

    # Now display the average K/D for Team Two
    team_kills = 0
    team_deaths = 0
    for hero in self.team_two.heroes:
        team_kills += hero.kills
        team_deaths += hero.deaths
    if team_deaths == 0:
        team_deaths = 1
    print(self.team_two.name + " average K/D was: " + str(team_kills/team_deaths))

    # Here is a way to list the heroes from Team One that survived
    for hero in self.team_one.heroes:
        if hero.deaths == 0:
            print("survived from " + self.team_one.name + ": " + hero.name)

    
    #Now list the heroes from Team Two that survived
     for hero in self.team_two.heroes:
        if hero.deaths == 0:
            print("survived from " + self.team_two.name + ": " + hero.name)