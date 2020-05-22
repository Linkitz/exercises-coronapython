# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
foods = ('Rice', 'Meat', 'Ram', 'Bean', 'Orange')
#
# • Use a for loop to print each food the restaurant offers.
for food in foods:
    print(food)
#
# • Try to modify one of the items, and make sure that Python rejects the change.
#food
#foods[2] = "Apple"
#
# • The restaurant changes its menu, replacing two of the items with different foods. Add a block of code that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
foods = ('Rice', 'Aplle', 'Pie', 'Bean', 'Orange')

for food in foods:
    print(food)