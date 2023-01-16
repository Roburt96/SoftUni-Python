first = int(input())
second = int(input())
magic = int(input())

counter = 0
found = False

for first_number in range(first, second + 1):
    for second_number in range(first, second +1):
        counter += 1
        if first_number + second_number == magic:
            print(f"Combination N:{counter} ({first_number} + {second_number} = {magic})")
            found = True
            break
    if found:
        break

if not found:
    print(f"{counter} combinations - neither equals {magic}")
