budget = float(input())
statistics = int(input())
cloth = float(input())

discount = 10 / 100
decor = budget * 0.10
cloth_price = statistics * cloth

#Ако статистите са повече от 150 получават 10% отстъпка.
if statistics > 150:
    cloth_price -= cloth_price * discount

movie = decor + cloth_price

if movie > budget:
    print("Not enough money!")
    print(f"Wingard needs{movie - budget: .2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with{budget - movie: .2f} leva left.")
