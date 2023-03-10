#Пъзел - 2.60 лв.
#Гоореща кукла - 3 лв.
#Плюено мече - 4.10 лв.
#Миньон - 8.20 лв.
#Камионче - 2 лв.

vacantion_trip = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

toys = puzzles + dolls + bears + minions + trucks
total = puzzles * 2.60 + dolls * 3.0 + bears * 4.10 + minions * 8.20 + trucks * 2.0

if toys >= 50:
    total -= total * 0.25

total -= total * 0.1

if total >= vacantion_trip:
    print(f"Yes! {total - vacantion_trip:.2f} lv left.")
else:
    print(f"Not enough money! {vacantion_trip - total:.2f} lv needed.")










