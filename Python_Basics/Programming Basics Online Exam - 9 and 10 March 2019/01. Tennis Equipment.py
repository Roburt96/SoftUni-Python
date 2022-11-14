import math

price_one_tennis_racket = float(input())
tennis_racket = int(input())
tennis_shoes = int(input())

racket_price = tennis_racket * price_one_tennis_racket
price_one_shoes = price_one_tennis_racket / 6
total_price_shoes = tennis_shoes * price_one_shoes
another_stuff = (racket_price + total_price_shoes) * 0.2
total_price = racket_price + total_price_shoes + another_stuff
djokovic_price = total_price / 8
sponsors_price = (total_price * 7) / 8

print(f"Price to be paid by Djokovic {math.floor(djokovic_price)}")
print(f"Price to be paid by sponsors {math.ceil(sponsors_price)}")
