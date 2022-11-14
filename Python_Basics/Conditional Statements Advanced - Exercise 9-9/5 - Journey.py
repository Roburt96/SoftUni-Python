budget = float(input())
season = input()
type = ""
price = 0.00

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = budget * 0.3
        type = "Camp"
    else:
        price = budget * 0.7
        type = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = budget * 0.4
        type = "Camp"
    else:
        price = budget * 0.8
        type = "Hotel"
else:
    destination = "Europe"
    price = budget * 0.9
    type = "Hotel"

print(f"Somewhere in {destination}")
print(f"{type} - {price:.2f}")
