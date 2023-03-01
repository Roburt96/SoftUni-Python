def shopping_cart(*args):
    meals = {
        'Soup': [],
        'Pizza': [],
        'Dessert': []
    }
    limit = {
        'Soup': 3,
        'Pizza': 4,
        'Dessert': 2
    }
    empty = True
    for cmd in args:
        if cmd == 'Stop':
            break
        meal, product = cmd
        if len(meals[meal]) < limit[meal]:
            if product not in meals[meal]:
                meals[meal].append(product)
                empty = False


    result = ""
    for key, value in sorted(meals.items(), key=lambda x: (-len(x[1]), x[0])):
        result += f"{key}:\n"
        for i in sorted(value):
            result += f"- {i}\n"
    if empty:
        return "No products in the cart!"
    return result





# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Soup', 'carrots'),
#     ('Pizza', 'cheese'),
#     ('Pizza', 'flour'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'mushrooms'),
#     ('Pizza', 'tomatoes'),
#     'Stop',
# ))

# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'ham'),
#     'Stop',
# ))

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))