chrys = int(input())
rose = int(input())
tulip = int(input())
season = input()
holiday = input()

price = 0
flowers = chrys + rose + tulip

if season == "Spring" or season == "Summer":
    price_chrys = chrys * 2
    price_rose = rose * 4.10
    price_tulip = tulip * 2.50
    if holiday == "Y":
        price = (price_tulip + price_rose + price_chrys) * 1.15
    else:
        price = price_tulip + price_rose + price_chrys
    if tulip > 7:
        price *= 0.95
elif season == "Autumn" or season == "Winter":
    price_chrys = chrys * 3.75
    price_rose = rose * 4.50
    price_tylip = tulip * 4.15
    if holiday == "Y":
        price = (price_tylip + price_rose + price_chrys) * 1.15
    else:
        price = price_tylip + price_rose + price_chrys
if rose >= 10 and season == "Winter":
    price *= 0.90

if flowers >= 20:
    price *= 0.80

arranging = price + 2.00

print(f"{arranging:.2f}")