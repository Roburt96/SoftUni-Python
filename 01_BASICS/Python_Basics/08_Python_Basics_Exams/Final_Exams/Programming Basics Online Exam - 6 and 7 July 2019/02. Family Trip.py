budget = float(input())
number_of_nights = int(input())
price_for_nights = float(input())
percent_coast = int(input())

discount = 0.95

if number_of_nights > 7:
    price_for_nights *= discount

night_price = price_for_nights * number_of_nights
coast = budget * percent_coast / 100
total_price = night_price + coast
money_left = abs(total_price - budget)
if total_price <= budget:
    print(f"Ivanovi will be left with {money_left:.2f} leva after vacation.")
elif total_price > budget:
    print(f"{money_left:.2f} leva needed.")
