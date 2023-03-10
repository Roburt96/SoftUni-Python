airplane_capacity = float(input())
counter = 0

while True:
    suitcase = input()

    if suitcase == "End":
        print("Congratulations! All suitcases are loaded!")
        break
    else:
        suitcase = float(suitcase)

    # if suitcase > airplane_capacity:
    #     print("No more space!")
    #     break

    if (counter + 1) % 3 == 0:
        # suitcase = round(suitcase + (suitcase * 10 / 100)) ERROR WILL CAUSE 90/100
        suitcase *= 1.1

    if suitcase > airplane_capacity:
        print("No more space!")
        break

    counter += 1
    airplane_capacity -= suitcase

print(f'Statistic: {counter} suitcases loaded.')