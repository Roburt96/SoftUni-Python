season = input()
km_month = float(input())

salary = 0

if season == "Spring" or "Autumn":
    if km_month <= 5000:
        salary = km_month * 0.75
    elif 5000 < km_month <= 10000:
        salary = km_month * 0.95
    else:
        salary = km_month * 1.45
if season == "Summer":
    if km_month <= 5000:
        salary = km_month * 0.9
    elif 5000 < km_month <= 10000:
        salary = km_month * 1.10
    else:
        salary = km_month * 1.45
if season == "Winter":
    if km_month <= 5000:
        salary = km_month * 1.05
    elif 5000 < km_month <= 10000:
        salary = km_month * 1.25
    else:
        salary = km_month * 1.45

price = (salary * 4) * 0.9
print(f"{price:.2f}")
