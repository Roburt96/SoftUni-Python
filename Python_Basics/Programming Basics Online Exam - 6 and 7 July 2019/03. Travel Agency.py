city_name = input()
kind_of_packet = input()
VIP_discount = input()
days = int(input())

price = 0

if days > 7:
    days -= 1

if not (city_name in ("Bansko", "Borovets") and kind_of_packet in ("noEquipment", "withEquipment",)) and not (
        city_name in ("Varna", "Burgas") and kind_of_packet in ("noBreakfast", "withBreakfast")):
    print(f'Invalid input!')

elif days < 1:
    print(f'Days must be positive number!')
else:
    if city_name == "Bansko" or city_name == "Borovets":
        if kind_of_packet == "withEquipment":
            price = days * 100
            if VIP_discount == "yes":
                price *= 0.90
        elif kind_of_packet == "noEquipment":
            price = days * 80
            if VIP_discount == "yes":
                price *= 0.95
    elif city_name == "Varna" or city_name == "Burgas":
        if kind_of_packet == "withBreakfast":
            price = days * 130
            if VIP_discount == "yes":
                price *= 0.88
        elif kind_of_packet == "noBreakfast":
            price = days * 100
            if VIP_discount == "yes":
                price *= 0.93

    print(f"The price is {price:.2f}lv! Have a nice time!")
