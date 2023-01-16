products = {}

def add_product_(name, price, quantity):
    if name in products:
        products[name]['price'] = price
        products[name]['quantity'] += quantity
    else:
        products[name] = products.get(name, {'price': 0, 'quantity': 0})
        products[name]['price'] = price
        products[name]['quantity'] = quantity


command = input()
while command != 'stocked':
    product_name, product_price, product_quantity = [float(x) if x[0].isdigit() else x for x in command.split()]
    add_product_(product_name, product_price, product_quantity)
    command = input()

total = 0
for name in products.keys():
    name_price = products[name]['price']
    name_quantity = products[name]['quantity']
    total += name_price * name_quantity
    print(f"{name}: ${name_price:.2f} * {int(name_quantity)} = ${name_price * name_quantity:.2f}")
print("------------------------------")
print(f"Grand Total: ${total:.2f}")