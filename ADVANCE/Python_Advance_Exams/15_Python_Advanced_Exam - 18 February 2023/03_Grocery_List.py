def shop_from_grocery_list(*args):
    budget = args[0]
    grocery_list = args[1]
    product = args[2:]

    for product, price in product:
        if grocery_list:
            if product in grocery_list:
                if budget >= price:
                    grocery_list.remove(product)
                    budget -= price
                elif budget < price:
                    break
        else:
            break

    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        result = ', '.join(grocery_list)
        return f"You did not buy all the products. Missing products: {result}."




print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))