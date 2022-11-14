season = input()
group = input()
students = int(input())
nights = int(input())

price = 0
sport = ""

if season == "Winter":
    if group == "boys":
        price = students * 9.60 * nights
        sport = "Judo"
    elif group == "girls":
        price = students * 9.60 * nights
        sport = "Gymnastics"
    elif group == "mixed":
        price = students * 10 * nights
        sport = "Ski"

if season == "Spring":
    if group == "boys":
        price = students * 7.20 * nights
        sport = "Tennis"
    elif group == "girls":
        price = students * 7.20 * nights
        sport = "Athletics"
    elif group == "mixed":
        price = students * 9.50 * nights
        sport = "Cycling"

if season == "Summer":
    if group == "boys":
        price = students * 15 * nights
        sport = "Football"
    elif group == "girls":
        price = students * 15 * nights
        sport = "Volleyball"
    elif group == "mixed":
        price = students * 20 * nights
        sport = "Swimming"

if students >= 50:
    price *= 0.5
elif 20 <= students < 50:
    price *= 0.85
elif 10 <= students < 20:
    price *= 0.95

print(f"{sport} {price:.2f} lv.")
