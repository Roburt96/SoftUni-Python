budget = float(input())
flour_1kg = float(input())
loaves = 0
colored_eggs = 0

price_pack_eggs = flour_1kg * 0.75
price_milk = flour_1kg * 1.25
bread_price = flour_1kg + price_pack_eggs + price_milk * 0.25

while budget >= bread_price:
    loaves += 1
    budget -= bread_price
    colored_eggs += 3
    if loaves % 3 == 0:
        colored_eggs -= (loaves - 2)
print(f'You made {loaves} loaves of Easter bread! Now '
      f'you have {colored_eggs} eggs and {budget:.2f}BGN left.')
