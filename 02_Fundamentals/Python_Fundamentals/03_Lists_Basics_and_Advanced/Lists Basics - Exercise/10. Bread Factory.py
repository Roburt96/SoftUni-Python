# orders = input().split("|")
# energy = 100
# coins = 100
# no_coins = False
#
# for clean_text in orders:
#     event_name, ingredient = [int(x) if x.isdigit() else x for x in clean_text.split("-")]
#     if event_name == "order":
#         if energy < 30:
#             print("You had to rest!")
#             energy += 50
#         else:
#             coins += ingredient
#             energy -= 30
#             print(f"You earned {ingredient} coins.")
#     elif event_name == "rest":
#         if energy + ingredient > 100:
#             print(f"You gained {abs(100 - energy)} energy.")
#             energy = 100
#         else:
#             energy += ingredient
#             print(f"You gained {ingredient} energy.")
#         print(f"Current energy: {energy}.")
#
#     elif event_name != "rest" or event_name != "work":
#         if coins >= ingredient:
#             print(f"You bought {event_name}.")
#             coins -= ingredient
#         elif coins < ingredient:
#             no_coins = True
#             break
#
# if no_coins:
#     print(f"Closed! Cannot afford {event_name}.")
# else:
#     print("Day completed!")
#     print(f"Coins: {coins}")
#     print(f"Energy: {energy}")




def rest_(energy_gain):
    global energy
    if energy + energy_gain > 100:
        print(f"You gained {abs(100 - energy)} energy.")
        energy = 100
    else:
        energy += energy_gain
        print(f"You gained {energy_gain} energy.")
    print(f"Current energy: {energy}.")


def order_(coin_gain):
    global energy, coins
    if energy >= 30:
        energy -= 30
        coins += coin_gain
        print(f"You earned {coin_gain} coins.")
    else:
        energy += 50
        print(f"You had to rest!")


def buy_(product_name, coin_spend):
    global coins, no_coins
    if coins >= coin_spend:
        print(f"You bought {product_name}.")
        coins -= coin_spend
    else:
        print(f"Closed! Cannot afford {product_name}.")
        no_coins = True


orders = input().split("|")
energy = 100
coins = 100
no_coins = False

for order in orders:
    order_type, order_number = order.split('-')

    if 'rest' in order_type:
        index_gain = int(order_number)
        rest_(index_gain)

    elif 'order' in order_type:
        coins_gain = int(order_number)
        order_(coins_gain)

    elif order_type != "rest" or order_type != "work":
        product_name = order_type
        product_count = int(order_number)
        buy_(product_name, product_count)

print("Day completed!")
print(f"Coins: {coins}")
print(f"Energy: {energy}")
















