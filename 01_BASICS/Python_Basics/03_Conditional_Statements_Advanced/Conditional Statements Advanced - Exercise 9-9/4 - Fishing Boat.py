budget = int(input())
season = input()
fisherman = int(input())
price = 0.00

if season == "Spring":
    if fisherman <= 6:
        price = 3000 * 0.90
    elif fisherman <= 11:
        price = 3000 * 0.85
    elif fisherman >= 12:
        price = 3000 * 0.75
if season == "Summer":
    if fisherman <= 6:
        price = 4200 * 0.90
    elif fisherman <= 11:
        price = 4200 * 0.85

    elif fisherman >= 12:
        price = 4200 * 0.75
if season == "Autumn":
    if fisherman <= 6:
        price = 4200 * 0.90
    elif fisherman <= 11:
        price = 4200 * 0.85
    else:
        price = 4200 * 0.75
if season == "Winter":
    if fisherman <= 6:
        price = 2600 * 0.90
    elif fisherman <= 11:
        price = 2600 * 0.85
    elif fisherman >= 12:
         price = 2600 * 0.75

if season != "Autumn" and fisherman % 2 ==0:
    price *=0.95

money_left = abs(budget - price)
if budget >= price:
    print(f"Yes! You have {money_left:.2f} leva left.")
elif budget <= price:
    print(f"Not enough money! You need {money_left:.2f} leva.")
