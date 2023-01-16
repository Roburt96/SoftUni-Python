budget = float(input())
destination = input()
season = input()
days = int(input())
price = 0

if destination == "Dubai":
    if season == "Winter":
        price = days * 45000
    elif season == "Summer":
        price = days * 40000

if destination == "Sofia":
    if season == "Winter":
        price = days * 17000
    elif season == "Summer":
        price = days * 12500

if destination == "London":
    if season == "Winter":
        price = days * 24000
    elif season == "Summer":
        price = days * 20250

if destination == "Dubai":
    price *= 0.70
if destination == "Sofia":
    overcharge = price * 0.25
    price += overcharge

if budget >= price:
    print(f"The budget for the movie is enough! We have {budget - price:.2f} leva left!")
if price > budget:
    print(f"The director needs {price - budget:.2f} leva more!")
