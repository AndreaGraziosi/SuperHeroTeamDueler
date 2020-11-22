#weapon.py
import random 


class Weapon(Ability):
    def weapons(self, value):
        half_max_value = self.max_damage//2
        weapond_value = random.randint(half_max_value, self.max_damage)
        return weapond_value

