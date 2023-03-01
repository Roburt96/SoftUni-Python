month = input()
overnight = int(input())
studio = 0
apartment = 0

if month == "May" or month == "October":
    studio = overnight * 50
    apartment = overnight * 65
    if overnight > 14:
        studio *= 0.7
    elif overnight > 7:
        studio *= 0.95

elif month == "June" or month == "September":
    studio = overnight * 75.2
    apartment = overnight * 68.7
    if overnight > 14:
        studio *= 0.8

elif month == "July" or month == "August":
    studio = overnight * 76
    apartment = overnight * 77

if 14 < overnight:
    apartment *= 0.9

print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")
