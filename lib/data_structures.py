spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names =  [food.get('name') for food in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    spiciest = [food for food in spicy_foods if food.get("heat_level") > 5]
    return spiciest

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f'{food.get("name")} ({food.get("cuisine")}) | Heat Level: {food.get("heat_level") * "🌶"}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if cuisine == food.get('cuisine'):
            return food

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food.get('heat_level') > 5:
            print(f'{food.get("name")} ({food.get("cuisine")}) | Heat Level: {food.get("heat_level") * "🌶"}')

def get_average_heat_level(spicy_foods):
    count = 0
    heat = 0
    for food in spicy_foods:
        count += 1
        heat += food.get('heat_level')
    return heat / count


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

