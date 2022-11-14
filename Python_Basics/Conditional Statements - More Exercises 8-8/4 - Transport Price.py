distance = int(input())
day_or_night = input()
price = 0.00
taxi_rate = 0.00

if day_or_night == "day":
    taxi_rate = 0.79
else:
    taxi_rate = 0.90

if distance < 20:
    price = (f"{0.70 + distance * taxi_rate:.2f}")
elif distance < 100:
    price = (f"{distance * 0.09:.2f}")
else:
    price = (f"{distance * 0.06:.2f}")

print(price)



