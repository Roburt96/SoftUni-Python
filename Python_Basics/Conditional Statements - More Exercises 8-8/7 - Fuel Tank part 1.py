fuel_type = input()
liters_fuel = int(input())

if fuel_type == "Diesel":
    if liters_fuel >= 25:
        print(f"You have enough {fuel_type.lower()}.")
    elif liters_fuel < 25:
        print(f"Fill your tank with {fuel_type.lower()}!")

elif fuel_type == "Gasoline":
    if liters_fuel >= 25:
        print(f"You have enough {fuel_type.lower()}.")
    elif liters_fuel < 25:
        print(f"Fill your tank with {fuel_type.lower()}!")

elif fuel_type == "Gas":
    if liters_fuel >= 25:
        print(f"You have enough {fuel_type.lower()}.")
    elif liters_fuel < 25:
        print(f"Fill your tank with {fuel_type.lower()}!")
else:
    print("Invalid fuel!")










