import tkinter as tk
import json

class Game_Item:
    def __init__(self, name, enchantments, anvil_uses, levels_spent=0):
        self.name = name
        self.enchantments = enchantments
        self.anvil_uses = anvil_uses
        self.levels_spent = levels_spent
    
    def get_ench_level(self, enchantment):
        return self.enchantments[enchantment] if enchantment in dict.keys(self.enchantments) else 0

    def add_enchantment(self, book, ench_data):
        total_cost = 0
        for enchantment in book.enchantments:
            total_cost += max(0, 1 if (book.enchantments[enchantment] == self.get_ench_level(enchantment)) and (self.get_ench_level(enchantment) != ench_data['enchants'][enchantment]['levelMax']) else book.enchantments[enchantment]-self.get_ench_level(enchantment))*ench_data['enchants'][enchantment]['weight']
            self.enchantments[enchantment] = self.get_ench_level(enchantment)+1 if (book.enchantments[enchantment] == self.get_ench_level(enchantment)) and (self.get_ench_level(enchantment) != ench_data['enchants'][enchantment]['levelMax']) else max(book.enchantments[enchantment], self.get_ench_level(enchantment))

        pu_penalty = ((2**self.anvil_uses)-1)+((2**book.anvil_uses)-1)
        self.anvil_uses = max(self.anvil_uses, book.anvil_uses)+1
        self.levels_spent += total_cost+pu_penalty+book.levels_spent
        return total_cost+pu_penalty

def find_combinations(primary_item, books):
    ## combination in format [book, book, book] in order to combine to item
    combinations = {}
    for i in range(len(books)-1): # num of brackets
        item_copy = Game_Item(primary_item.name, primary_item.enchantments, primary_item.anvil_uses, primary_item.levels_spent)

with open('data.json', 'r') as raw_data:
    ench_data = json.load(raw_data)

primary_item = Game_Item('shovel', {}, 0)
enchantments_to_add = [Game_Item('book', {'mending': 1}, 0), Game_Item('book', {'efficiency': 3}, 0)] # Enchantments as Dict with the enchantment and level, e.g {'looting': 2}
