fuel_type = input()
liters_fuel = float(input())
club_card = input()
price = float()

if club_card == "Yes" and fuel_type == "Gas":
    if liters_fuel > 25:
        discount = (liters_fuel * (0.93 - 0.08)) * 0.10
        price = (liters_fuel * (0.93 - 0.08)) - discount
    elif 20 < liters_fuel <= 25:
        discount = liters_fuel * (0.93 - 0.08) * 0.08
        price = liters_fuel * (0.93 - 0.08) - discount
    else:
        price = 0.93 * liters_fuel
if club_card == "No" and fuel_type == "Gas":
    if liters_fuel > 25:
        discount = (liters_fuel * 0.93) * 0.10
        price = (liters_fuel * 0.93) - discount
    elif 20 < liters_fuel <= 25:
        price = liters_fuel * (0.93 - 0.08)
    else:
        price = liters_fuel * 0.93
if club_card == "Yes" and fuel_type == "Gasoline":
    if liters_fuel > 25:
        discount = (liters_fuel * (2.22 - 0.18)) * 0.10
        price = (liters_fuel * (2.22 - 0.18)) - discount
    elif 20 < liters_fuel <= 25:
        discount = (liters_fuel * (2.22 - 0.18)) * 0.08
        price = (liters_fuel * (2.22 - 0.18)) - discount
    else:
        price = liters_fuel * 2.22
if club_card == "No" and fuel_type == "Gasoline":
    if liters_fuel > 25:
        discount = (liters_fuel * 2.22) * 0.10
        price = (liters_fuel * 2.22) - discount
    elif 20 < liters_fuel <= 25:
        discount = (liters_fuel * 2.22) * 0.08
        price = (liters_fuel * 2.22) - discount
    else:
        price = liters_fuel * 2.22
if club_card == "Yes" and fuel_type == "Diesel":
    if liters_fuel > 25:
        discount = (liters_fuel * (2.33 - 0.12)) * 0.10
        price = (liters_fuel * (2.33 - 0.12)) - discount
    elif 20 < liters_fuel <= 25:
        discount = (liters_fuel * (2.33 - 0.12)) * 0.08
        price = (liters_fuel * (2.33 - 0.12)) - discount
    else:
        price = liters_fuel * 2.33
if club_card == "No" and fuel_type == "Diesel":
    if liters_fuel > 25:
        discount = (liters_fuel * 2.33) * 0.10
        price = (liters_fuel * 2.33) - discount
    elif 20 < liters_fuel <= 25:
        discount = (liters_fuel * 2.33) * 0.08
        price = (liters_fuel * 2.33) - discount
    else:
        price = liters_fuel * 2.33

print(f'{price:.2f} lv.')
