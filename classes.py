class Game_Item:
    def __init__(self, name, enchantments, anvil_uses, levels_spent=0):
        self.name = name
        self.enchantments = enchantments
        self.anvil_uses = anvil_uses
        self.levels_spent = levels_spent
        self.min_xp = 0

    def __str__(self):
        return f'{self.name}:\nEnchantments: {self.enchantments}\nAnvil Uses: {self.anvil_uses}\nLevels Required: {self.levels_spent} ({self.min_xp}-{self.xpCostToAdd(self.levels_spent)}xp)'
    
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
        self.min_xp += self.xpCostToAdd(total_cost+pu_penalty)+book.min_xp
        return total_cost+pu_penalty
    
    def xpCostToAdd(self, levels):
        xpCost = 0
        if levels <= 16:
            xpCost = (levels**2)+(6*levels)
        elif levels <= 31:
            xpCost = (2.5*((levels)**2))-(40.5*(levels))+360
        else:
            xpCost = (4.5*((levels)**2))-(162.5*(levels))+2220
        return int(xpCost)