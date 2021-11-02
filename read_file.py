from pprint import pprint

import os
print()
path = os.path.join(os.getcwd(), 'recipes.txt')
# print(path)
print()
with open(path) as file:
    result = {}
    for dish in file:
        dish_name = dish.strip()
        counter = int(file.readline().strip())
        temp_data = []
        for item in range(counter):
            ingredient_name, quantity, measure = file.readline().split(' | ')
            temp_data.append(
                {"ingredient_name": ingredient_name.strip(), "quantity": int(quantity), "measure": measure.strip()}
            )
        result[dish_name] = temp_data
        file.readline()
    pprint(result)
    