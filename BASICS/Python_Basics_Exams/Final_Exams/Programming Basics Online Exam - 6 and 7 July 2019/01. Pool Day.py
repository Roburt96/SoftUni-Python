import math

people = int(input())
entrance_tax = float(input())
price_for_one_sunbed = float(input())
price_for_one_umbrella = float(input())

tax = people * entrance_tax
sunbed = math.ceil(people * 0.75)
sunbed_price = sunbed * price_for_one_sunbed
umbrella_needed = math.ceil(people * 0.50)
umbrella_price = umbrella_needed * price_for_one_umbrella

total_price = tax + sunbed_price + umbrella_price
print(f"{total_price:.2f} lv.")
