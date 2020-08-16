class CoffeeTypes:
    types = []

    def __init__(self, name, cost, water, coffee_beans, milk=0):
        self.dictionary = {'name': name, 'water': water, 'coffee beans': coffee_beans, 'milk': milk, 'cost': cost}
        CoffeeTypes.types.append(self.dictionary)


espresso = CoffeeTypes("Espresso", 4, 250, 16)
latte = CoffeeTypes("Latte", 7, 350, 20, 75)
cappuccino = CoffeeTypes("Cappuccino", 6, 200, 12, 200)

for types in CoffeeTypes.types:
    for keys, values in types.items():
        print(keys, ":", values)

# coffee_types = []
#
# cappuccino = {'name': 'Cappuccino', 'water': 250, 'coffee_beans': 16, 'milk': 200, 'cost': 4}
# espresso = {'name': 'Espresso', 'water': 250, 'coffee_beans': 16, 'milk': 0, 'cost': 5}
# latte = {'name': 'Latte', 'water': 350, 'coffee_beans': 20, 'milk': 75, 'cost': 7}
#
# coffee_types.append(cappuccino)
# coffee_types.append(espresso)
# coffee_types.append(latte)
#
# for types in coffee_types:
#     for keys, values in types.items():
#         print(keys, ": ", values)
