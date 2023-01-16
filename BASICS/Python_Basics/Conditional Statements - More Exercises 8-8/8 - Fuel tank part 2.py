fuel_type = str(input())
liters_fuel = float(input())
club_card = str(input())
price = float()

if club_card == "Yes" and fuel_type == "Gas":
    if liters_fuel > 25:
        price = 0.9*(0.85 * liters_fuel)
    elif 20 < liters_fuel <= 25:
        price = 0.92*(0.85 * liters_fuel)
    else:
        price = 0.85 * liters_fuel
if club_card == "No" and fuel_type == "Gas":
    if liters_fuel > 25:
        price = 0.9 * (0.93 * liters_fuel)
    elif 20 < liters_fuel <= 25:
        price = 0.92 * (0.93 * liters_fuel)
    else:
        price = liters_fuel * 0.93
if club_card == "Yes" and fuel_type == "Gasoline":
    if liters_fuel > 25:
        price = 0.9*(2.04 * liters_fuel)
    elif 20 < liters_fuel <= 25:
        price = 0.92*(2.04 * liters_fuel)
    else:
        price = liters_fuel * 2.04
if club_card == "No" and fuel_type == "Gasoline":
    if liters_fuel > 25:
        price = 0.9 * (2.22 * liters_fuel)
    elif 20 < liters_fuel <= 25:
        price = 0.92 * (2.22 * liters_fuel)
    else:
        price = liters_fuel * 2.22
if club_card == "Yes" and fuel_type == "Diesel":
    if liters_fuel > 25:
        price = 0.9*(2.21 * liters_fuel)
    elif 20 < liters_fuel <= 25:
        price = 0.92*(2.21 * liters_fuel)
    else:
        price = liters_fuel * 2.21
if club_card == "No" and fuel_type == "Diesel":
    if liters_fuel > 25:
        price = 0.9 * (2.33 * liters_fuel)
    elif 20 < liters_fuel <= 25:
        price = 0.92 * (2.33 * liters_fuel)
    else:
        price = liters_fuel * 2.33

print(f'{price:.2f} lv.')
