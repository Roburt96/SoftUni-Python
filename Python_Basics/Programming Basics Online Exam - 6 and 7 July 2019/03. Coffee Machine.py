drink = input()
sugar = input()
number_of_drinks = int(input())

without_sugar = 0.65
price = 0

if drink == "Espresso":
    if sugar == "Without":
        price = number_of_drinks * 0.90
    elif sugar == "Normal":
        price = number_of_drinks * 1
    elif sugar == "Extra":
        price = number_of_drinks * 1.20
if drink == "Cappuccino":
    if sugar == "Without":
        price = number_of_drinks * 1
    elif sugar == "Normal":
        price = number_of_drinks * 1.20
    elif sugar == "Extra":
        price = number_of_drinks * 1.60
if drink == "Tea":
    if sugar == "Without":
        price = number_of_drinks * 0.50
    elif sugar == "Normal":
        price = number_of_drinks * 0.60
    elif sugar == "Extra":
        price = number_of_drinks * 0.70

if sugar == "Without":
    price *= without_sugar
if drink == "Espresso" and number_of_drinks >= 5:
    price *= 0.75
if price > 15:
    price *= 0.80

print(f"You bought {number_of_drinks} cups of {drink} for {price:.2f} lv.")
