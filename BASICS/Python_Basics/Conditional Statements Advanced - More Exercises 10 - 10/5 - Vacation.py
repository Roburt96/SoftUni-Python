budget = float(input())
season = input()

price = 0
place = ""
location = ""


if budget <= 1000 and season == "Summer":
    place = "Camp"
    location = "Alaska"
    price = budget * 0.65
elif budget <= 1000 and season == "Winter":
    place = "Camp"
    location = "Morocco"
    price = budget * 0.45

if 1000 < budget <= 3000 and season == "Summer":
    place = "Hut"
    location = "Alaska"
    price = budget * 0.80
elif 1000 < budget <= 3000 and season == "Winter":
    place = "Hut"
    location = "Morocco"
    price = budget * 0.60

if budget > 3000 and season == "Summer":
    place = "Hotel"
    location = "Alaska"
    price = budget * 0.90
elif budget > 3000 and season == "Winter":
    place = "Hotel"
    location = "Morocco"
    price = budget * 0.90

print(f"{location} - {place} - {price:.2f}")
