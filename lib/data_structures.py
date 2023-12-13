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
    names = []
    for food in spicy_foods:
        names.append(food['name'])
    return names
    # return [food['name'] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    items = []
    for food in spicy_foods:
        if food['heat_level'] >= 5:
            items.append(food)
    return items

def print_spicy_foods(spicy_foods):
    printed_foods = []
    for food in spicy_foods:
        name = food['name'] 

        cuisine = food['cuisine']

        heat = food['heat_level']
        emoji = '🌶'
        heat_emoji = heat * emoji

        printed_foods = print(f'{name} ({cuisine}) | Heat Level: {heat_emoji}')
        
    return printed_foods

# print_spicy_foods(spicy_foods)


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    get_foods = {}
    for food in spicy_foods:
        if cuisine == food['cuisine']:
            get_foods = (food)
    return get_foods

get_spicy_food_by_cuisine(spicy_foods, 'American')
print(get_spicy_food_by_cuisine(spicy_foods, 'American'))


def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        name = food['name'] 
        cuisine = food['cuisine']
        heat = food['heat_level']
        emoji = '🌶'
        heat_emoji = heat * emoji

        if food['heat_level'] >= 5:
            print(f'{name} ({cuisine}) | Heat Level: {heat_emoji}')
        
print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    pass

def create_spicy_food(spicy_foods, spicy_food):
    pass
