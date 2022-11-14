orders = int(input())
total = 0

for sum in range(orders):
    price_capsule = float(input())
    days = int(input())
    capsules_day = int(input())
    if price_capsule < 0.01 or price_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_day < 1 or capsules_day > 2000:
        continue
    order_price = price_capsule * days * capsules_day
    total += order_price
    print(f'The price for the coffee is: ${order_price:.2f}')

print(f'Total: ${total:.2f}')
