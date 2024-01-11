import json
import classes
import functions

with open('data.json', 'r') as raw_data:
    ench_data = json.load(raw_data)

primary_item = classes.Game_Item('shovel', {}, 0)
enchantments_to_add = [classes.Game_Item('book', {'mending': 1}, 0), classes.Game_Item('book', {'efficiency': 3}, 0), classes.Game_Item('book', {'unbreaking': 3}, 0), classes.Game_Item('book', {'silk_touch': 1}, 0)] # Enchantments as Dict with the enchantment and level, e.g {'looting': 2}

combination = functions.find_combinations(primary_item, enchantments_to_add, ench_data)
print(combination[0]) # Item w/ enchantments
print(f'Books: {[book for book in functions.createBrackets(combination[1][0], combination[1][1])]}') # Show bracket locations
print(combination[1][1]) # Brackets
