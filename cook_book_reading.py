from pprint import pprint

import os
print()
def unload_cook_book():
    path = os.path.join(os.getcwd(), 'recipes.txt')

    with open(path) as file:
        cook_book = {}
        
        for dish in file:
            dish_name = dish.strip()
            ingredients = int(file.readline().strip())
            data_of_dish = []
            for igt in range(ingredients):
                ingredient_name, quantity, unit = file.readline().split(' | ')
                data_of_dish.append(
                    {'ingredient_name' : ingredient_name.strip(), 'quantity' : int(quantity.strip()), 'unit' : unit.strip()}
                )
                # print(data_of_dish)
            cook_book[dish_name] = data_of_dish
            file.readline()
        # print('cook_book =')
        return cook_book

pprint(unload_cook_book())
print()
dishes = []
def get_shop_list_by_dishes(dishes, person_count):
        
    dishes_order = {}
    for dish in dishes:
        for recipe in unload_cook_book()[dish]:
            if recipe['ingredient_name'] in dishes_order.keys():
                dishes_order[recipe['ingredient_name']]['quantity'] += recipe['quantity'] * person_count
            else:
                dishes_order[recipe['ingredient_name']] = {}
                dishes_order[recipe['ingredient_name']]['unit'] = recipe['unit']
                dishes_order[recipe['ingredient_name']]['quantity'] = recipe['quantity'] * person_count
    return dishes_order


pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))


