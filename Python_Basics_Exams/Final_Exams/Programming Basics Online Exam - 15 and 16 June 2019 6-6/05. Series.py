Thrones = 0.50
Lucifer = 0.40
Protector = 0.30
TotalDrama = 0.20
Area = 0.10
total_price = 0

budget = float(input())
number_of_serials = int(input())

for i in range(0, number_of_serials):
    name_of_serial = input()
    price_for_serial = float(input())

    if name_of_serial == "Thrones":
        price = price_for_serial - (price_for_serial * Thrones)
        total_price += price
    elif name_of_serial == "Lucifer":
        price = price_for_serial - (price_for_serial * Lucifer)
        total_price += price
    elif name_of_serial == "Protector":
        price = price_for_serial - (price_for_serial * Protector)
        total_price += price
    elif name_of_serial == "TotalDrama":
        price = price_for_serial - (price_for_serial * TotalDrama)
        total_price += price
    elif name_of_serial == "Area":
        price = price_for_serial - (price_for_serial * Area)
        total_price += price
    else:
        total_price += price_for_serial

money_left = abs(budget - total_price)

if budget >= total_price:
    print(f"You bought all the series and left with {money_left:.2f} lv.")
elif budget < total_price:
    print(f"You need {money_left:.2f} lv. more to buy the series!")
