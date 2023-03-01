number_of_cities = int(input())
total_money = 0
total_per_city = 0
profit = 0
expense = 0
for city in range(1, number_of_cities + 1):

    name_of_city = input()
    income = float(input())
    expenses = float(input())

    profit += income
    expense += expenses
    if city % 3 == 0:
        expense += expenses - (expenses * 0.50)
    elif city % 5 == 0:
        profit -= profit - (profit * 0.10)
    total_per_city = profit - expense
    total_money += total_per_city
    print(f"In {name_of_city} Burger Bus earned {total_per_city:.2f} leva.")
    total_per_city = 0
    profit = 0
    expense = 0

print(f"Burger Bus total profit: {total_money:.2f} leva.")

