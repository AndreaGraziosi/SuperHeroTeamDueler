#armor.py
import random

class Armor:
    def __init__(self, name, max_block):
        """Instantiate instance properties"""
        self.name = name
        self.max_block = max_block




    def block(self):
        """calculate the amount we block with"""
        block_power = random.randint(0, self.max_block)
        return block_power




if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    armor = Armor("Debugging Shield", 10)
    print(armor.name)
    print(armor.block())