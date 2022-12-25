def shopping_list(budget, **kwargs):
    buy_product = []
    budget_left = budget
    if budget < 100:
        return "You do not have enough budget."
    for key, value in kwargs.items():
        product_name = key
        product_value = value[0] * value[1]
        if budget >= product_value and len(buy_product) < 5:
            budget -= product_value
            buy_product.append(f"You bought {product_name} for {product_value:.2f} leva.")
    return "\n".join(buy_product)







# print(shopping_list(20,
#                     jeans=(19.99, 1),
#                     ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))

#
# print(shopping_list(100,
#                     microwave=(70, 2),
#                     skirts=(15, 4),
#                     coffee=(1.50, 10),
#                     ))