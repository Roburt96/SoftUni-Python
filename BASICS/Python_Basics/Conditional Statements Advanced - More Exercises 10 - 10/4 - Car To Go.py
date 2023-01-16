budget = float(input())
season = input()

price = 0
class_car = ""
car = ""

if budget <= 100 and season == "Summer":
    class_car = "Economy class"
    car = "Cabrio"
    price = budget * 0.35
else:
    class_car = "Economy class"
    car = "Jeep"
    price = budget * 0.65

if budget > 100 and budget <= 500 and season == "Summer":
    class_car = "Compact class"
    car = "Cabrio"
    price = budget * 0.45
else:
    class_car = "Compact class"
    car = "Jeep"
    price = budget * 0.80

if budget > 500:
    class_car = "Luxury class"
    car = "Jeep"
    price = budget * 0.90

print(f"{class_car}")
print(f"{car} - {price:.2f}")
