kind_of_flowers = input()
number_of_flowers = int(input())
budget = int(input())
price = 0

if kind_of_flowers == "Roses":
    if number_of_flowers > 80:
        price = (number_of_flowers * 5)*0.9
    else:
        price = number_of_flowers * 5
if kind_of_flowers == "Dahlias":
    if number_of_flowers > 90:
        price = (number_of_flowers * 3.8)*0.85
    else:
        price = number_of_flowers * 3.8
if kind_of_flowers == "Tulips":
    if number_of_flowers > 80:
        price = (number_of_flowers * 2.8)*0.85
    else:
        price = number_of_flowers * 2.8
if kind_of_flowers == "Narcissus":
    if number_of_flowers < 120:
        price = number_of_flowers * 3 + (number_of_flowers * 3)*0.15
    else:
        price = number_of_flowers * 3
if kind_of_flowers == "Gladiolus":
    if number_of_flowers < 80:
        price = number_of_flowers * 2.5 + (number_of_flowers * 2.5)*0.20
    else:
        price = number_of_flowers * 2.50

money_left = abs(budget - price)
if budget >= price:
    print(f"Hey, you have a great garden with {number_of_flowers} {kind_of_flowers} and {money_left:.2f} leva left.")
elif budget < price:
    print(f"Not enough money, you need {money_left:.2f} leva more.")


