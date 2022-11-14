# orders_quantity = {}
# orders_prices = {}
# command = input()
# while command != "buy":
#     command = command.split()
#     product_name = command[0]
#     product_price = float(command[1])
#     product_quantity = int(command[2])
#
#     if product_name not in orders_dict:
#         orders_quantity[product_name] = 0
#         orders_quantity[product_name] = product_quantity
#         orders_prices[product_name] = 0
#         orders_prices[product_name] += product_price
#
#     else:
#         orders_quantity[product_name] += product_quantity
#         orders_prices[product_name] = product_price
#
#     command = input()
#
# # x = key -> '0' = value ---> key: value * key: value for all keys in dict.
# result = {x: orders_quantity.get(x, 0) * orders_prices.get(x, 0) for x in orders_dict}
#
# for key, value in result.items():
#     print(f"{key} -> {value:.2f}")


orders_dict = {}
command = input()
while command != "buy":
    command = command.split()
    product_name = command[0]
    product_price = float(command[1])
    product_quantity = int(command[2])

    orders_dict[product_name] = orders_dict.get(product_name, {'price': product_price, 'quantity': product_quantity})
    if orders_dict[product_name]['price'] != product_price:
        orders_dict[product_name]['price'] = product_price
        orders_dict[product_name]['quantity'] += product_quantity


    command = input()

for key in orders_dict:
    print(f"{key} -> {orders_dict[key]['price'] *  orders_dict[key]['quantity']:.2f} ")

