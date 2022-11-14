import math

magnolia = int(input())
hyacinths = int(input())
roses = int(input())
cactus = int(input())
gift = float(input())

price = magnolia * 3.25 + hyacinths * 4 + roses * 3.50 + cactus * 8
taxes = price * 0.05
profit = price - taxes
remaining = abs(gift - profit)
up = math.ceil(remaining)
down = math.floor(remaining)

if gift >= profit:
    print(f"She will have to borrow {up} leva.")
else:
    print(f"She is left with {down} leva.")
