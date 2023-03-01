
from collections import deque

textiles = deque(int(x) for x in input().split())
medicaments = deque(int(x) for x in input().split())

items = {
    'Patch': 30,
    'Bandage': 40,
    'MedKit': 100
}
created_items = {
    'Patch': 0,
    'Bandage': 0,
    'MedKit': 0
}
while textiles and medicaments:
    cur_textile = textiles.popleft()
    cur_medicament = medicaments.pop()

    total = cur_textile + cur_medicament

    if total in items.values():
        for item, value in items.items():
            if value == total:
                created_items[item] += 1
                break
        continue

    if total > items['MedKit']:
        created_items['MedKit'] += 1
        remaining = total - items['MedKit']
        medicaments[-1] += remaining

    else:
        cur_medicament += 10
        medicaments.append(cur_medicament)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
    for item, value in sorted(created_items.items(), key=lambda x: (-x[-1], x[0])):
        if value > 0:
            print(f"{item} - {value}")

elif not textiles:
    reversed_med = [int(x) for x in reversed(medicaments)]
    print("Textiles are empty.")
    for item, value in sorted(created_items.items(), key=lambda x: (-x[-1], x[0])):
        if value > 0:
            print(f"{item} - {value}")
    print(f"Medicaments left: {', '.join(str(x) for x in reversed_med)}")

elif not medicaments:
    print("Medicaments are empty.")
    for item, value in sorted(created_items.items(), key=lambda x: (-x[-1], x[0])):
        if value > 0:
            print(f"{item} - {value}")
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")






