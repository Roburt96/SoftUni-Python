from collections import deque

food = deque(int(x) for x in input().split(", "))   # pop
stamina = deque(int(x) for x in input().split(", "))  # popleft
days = 7

peaks = {
    'Vihren': {'level': 80},
    'Kutelo': {'level': 90},
    'Banski Suhodol': {'level': 100},
    'Polezhan': {'level': 60},
    'Kamenitza': {'level': 70}
}

completed = []


while food and stamina and days > 1:
    current_food = food.pop()
    current_stamina = stamina.popleft()
    total = current_food + current_stamina

    for key, value in peaks.items():

        if total >= value['level']:
            completed.append(key)
            peaks.pop(key)
            days -= 1
        break


if len(peaks) == 0:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print(f"Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if len(completed) > 0:
    print("Conquered peaks:")
    for key in completed:
        print(f"{key}")







