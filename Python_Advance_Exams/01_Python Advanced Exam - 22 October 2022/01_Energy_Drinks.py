from collections import deque
ml_of_caffeine = deque([int(x) for x in input().split(", ")])
energy_drinks = deque([int(x) for x in input().split(", ")])
start = 0

while ml_of_caffeine and energy_drinks:
    current_caffeine = ml_of_caffeine.pop()
    current_drink = energy_drinks.popleft()
    total = current_caffeine * current_drink

    if 300 >= start + total:
        start += total
        continue
    else:
        energy_drinks.append(current_drink)
        start -= 30
        if start < 0:
            start = 0



if len(energy_drinks) > 0:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {start} mg caffeine.")