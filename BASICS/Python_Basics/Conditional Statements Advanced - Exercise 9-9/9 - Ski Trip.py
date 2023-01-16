days_of_stay = int(input())
what_room = input()
ratting = input()
price = 0

if what_room == "room for one person":
    price = (days_of_stay - 1) * 18
elif what_room == "apartment":
    if days_of_stay < 10:
        price = ((days_of_stay - 1) * 25)*0.7
    elif 10 <= days_of_stay <= 15:
        price = ((days_of_stay - 1) * 25)*0.65
    else:
        price = ((days_of_stay - 1) * 25)*0.5
elif what_room == "president apartment":
    if days_of_stay < 10:
        price = (days_of_stay * 35)*0.9
    elif 10 <= days_of_stay <= 15:
        price = ((days_of_stay - 1) * 35)*0.85
    else:
        price = ((days_of_stay - 1) * 35)*0.8

if ratting == "positive":
    price += price * 0.25
else:
    price -= price * 0.1

print(f"{price:.2f}")
