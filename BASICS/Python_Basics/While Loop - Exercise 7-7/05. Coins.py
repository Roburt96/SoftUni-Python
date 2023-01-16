change = float(input())
number_of_coins = 0

change = int(change * 100)

while change > 0:
    if change - 200 >= 0:
        change -= 200
        number_of_coins += 1
    elif change - 100 >= 0:
        change -= 100
        number_of_coins += 1
    elif change - 50 >= 0:
        change -= 50
        number_of_coins += 1
    elif change - 20 >= 0:
        change -= 20
        number_of_coins += 1
    elif change - 10 >= 0:
        change -= 10
        number_of_coins += 1
    elif change - 5 >= 0:
        change -= 5
        number_of_coins += 1
    elif change - 2 >= 0:
        change -= 2
        number_of_coins += 1
    elif change - 1 >= 0:
        change -= 1
        number_of_coins += 1
        break

print(number_of_coins)
