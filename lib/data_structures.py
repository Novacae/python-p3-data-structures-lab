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

new_food = {
    "name": "Griot",
    "cuisine": "Haitian",
    "heat_level": 10,
}

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
  return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
     for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        heat_level_emoji = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {heat_level_emoji}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None


def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            name = food["name"]
            cuisine = food["cuisine"]
            heat_level_emoji = "🌶" * food["heat_level"]
            print(f"{name} ({cuisine}) | Heat Level: {heat_level_emoji}")

def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0

    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    num_spicy_foods = len(spicy_foods)
    average_heat = total_heat_level / num_spicy_foods

    return int(average_heat)

def create_spicy_food(spicy_foods, new_food):
     new_spicy_foods = spicy_foods.copy()
     new_spicy_foods.append(new_food)
     return new_spicy_foods
