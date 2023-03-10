buy_item = input().split("|")
budget = int(input())
item_price = list()
item_sell = list()
ticket = 150
budget_left = budget


for clean_text in buy_item:
    type_item, price_item = clean_text.split("->")
    price = float(price_item)
    if budget_left >= price:
        if any(["Clothes" in type_item and price < 50, "Shoes" in type_item
                and price < 35, "Accessories" in type_item and price < 20,5]):
            item_price.append(price)
            budget_left -= price
            item_sell.append(price * 1.40)


difference = sum(item_sell) - sum(item_price)
for n in item_sell:
    print(f"{n:.2f}", end=" ")

print(f"\nProfit: {difference:.2f}")
if budget + difference > ticket:
    print(f"Hello, France!")
else:
    print("Not enough money.")


