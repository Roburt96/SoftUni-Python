text = input()
ticket = input()
number_of_ticket = int(input())
picture = input()
price = 0
photo_sum = 0
photo = False

if text == "Quarter final":
    if ticket == "Standard":
        price = number_of_ticket * 55.50
    elif ticket == "Premium":
        price = number_of_ticket * 105.20
    elif ticket == "VIP":
        price = number_of_ticket * 118.90

if text == "Semi final":
    if ticket == "Standard":
        price = number_of_ticket * 75.88
    elif ticket == "Premium":
        price = number_of_ticket * 125.22
    elif ticket == "VIP":
        price = number_of_ticket * 300.40

if text == "Final":
    if ticket == "Standard":
        price = number_of_ticket * 110.10
    elif ticket == "Premium":
        price = number_of_ticket * 160.66
    elif ticket == "VIP":
        price = number_of_ticket * 400

if price > 4000:
    price *= 0.75
    photo = True
elif price > 2500:
    price *= 0.90

if picture == "Y":
    photo_sum += number_of_ticket * 40
    price += photo_sum
    if photo:
        price -= photo_sum
elif picture == "N":
    price = price

print(f"{price:.2f}")
