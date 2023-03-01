project = input()
project_pack = input()
tickets = int(input())
price = 0

if project == "John Wick":
    if project_pack == "Drink":
        price = tickets * 12
    elif project_pack == "Popcorn":
        price = tickets * 15
    elif project_pack == "Menu":
        price = tickets * 19

if project == "Star Wars":
    if project_pack == "Drink":
        price = tickets * 18
    elif project_pack == "Popcorn":
        price = tickets * 25
    elif project_pack == "Menu":
        price = tickets * 30

if project == "Jumanji":
    if project_pack == "Drink":
        price = tickets * 9
    elif project_pack == "Popcorn":
        price = tickets * 11
    elif project_pack == "Menu":
        price = tickets * 14

if project == "Star Wars" and tickets >= 4:
    price *= 0.70
if project == "Jumanji" and tickets == 2:
    price *= 0.85

print(f"Your bill is {price:.2f} leva.")
