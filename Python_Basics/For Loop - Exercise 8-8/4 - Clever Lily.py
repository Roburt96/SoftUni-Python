age = int(input())
price_laundry = float(input())
price_toy = int(input())
birthday_sum = 0
toys_count = 0
brother_fee = 0
present_money = 10
count_sum = 0

for i in range(1, age + 1):

    if i % 2 == 0:
        count_sum += 1
        birthday_sum += present_money * count_sum
        brother_fee += 1
    else:
        toys_count += 1

total_saved = birthday_sum + (toys_count * price_toy) - brother_fee
if total_saved >= price_laundry:
    total_saved = total_saved - price_laundry
    print(f"Yes! {total_saved:.2f}")
elif price_laundry > total_saved:
    price_laundry = price_laundry - total_saved
    print(f"No! {price_laundry:.2f}")
