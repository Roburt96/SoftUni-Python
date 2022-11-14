#Видеокарта – 250 лв./бр.

#Процесор – 35% от цената на закупените видеокарти/бр.

#Рам памет – 10% от цената на закупените видеокарти/бр

budget = float(input())
videocard = int(input())
processor = int(input())
ram = int(input())
discount = 15 / 100

price_videocard = videocard * 250
proces = price_videocard * 0.35
price_processor = proces * processor
ram_price = price_videocard * 0.10
price_ram = ram_price * ram
all_price = price_videocard + price_processor + price_ram


if videocard > processor:
    all_price -= all_price * discount



if all_price <= budget:
    print(f"You have{budget - all_price: .2f} leva left!")
else:
    print(f"Not enough money! You need{all_price - budget: .2f} leva more!")



