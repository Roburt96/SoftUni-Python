order = input()
total = int(input())


def water(price_water):
    print(f"{total * price_water:.2f}")


def coffee(price_coffee):
    print(f"{total * price_coffee:.2f}")


def coke(price_coke):
    print(f"{total * price_coke:.2f}")


def snacks(price_snacks):
    print(f"{total * price_snacks:.2f}")


if order == 'water':
    water(1.00)

elif order == 'coffee':
    coffee(1.50)

elif order == 'coke':
    coke(1.40)

elif order == 'snacks':
    snacks(2.00)





