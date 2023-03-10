needed_sum = int(input())
total_sum = 0
counter = 0
counter_Card = 0
counter_Cash = 0
card_money = 0
cash_money = 0
pays = 0
while needed_sum > total_sum:
    command = input()

    if command == "End":
        break
    pays += 1
    money = int(command)

    if pays % 2 != 0:
        if money > 100:
            print("Error in transaction!")
        else:
            total_sum += money
            cash_money += money
            counter_Cash += 1
            print("Product sold!")
    else:
        if money < 10:
            print("Error in transaction!")
        else:
            total_sum += money
            card_money += money
            counter_Card += 1
            print("Product sold!")


average_cs = 0.0
if counter_Cash > 0:
    average_cs = cash_money / counter_Cash
average_cc = 0.0
if counter_Card > 0:
    average_cc = card_money / counter_Card

if needed_sum <= total_sum:
    print(f"Average CS: {average_cs:.2f}")
    print(f"Average CC: {average_cc:.2f}")
else:
    print("Failed to collect required money for charity.")
