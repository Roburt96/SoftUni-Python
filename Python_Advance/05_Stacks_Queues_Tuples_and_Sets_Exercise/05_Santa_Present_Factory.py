from collections import deque
presents = {
    "Doll": {'need': 150, 'count': 0},
    "Wooden train": {'need': 250, 'count': 0},
    "Teddy bear": {'need': 350, 'count': 0},
    "Bicycle": {'need': 400, 'count': 0}
}
need = {
    150: "Doll",
    250: "Wooden train",
    350: "Teddy bear",
    400: "Bicycle"
}

materials = deque(int(x) for x in input().split())   # pop
magic = deque(int(x) for x in input().split())       # popleft

while materials and magic:
    if materials[-1] == 0 or magic[1] == 0:
        if materials[-1] == 0:
            materials.pop()
        if magic[0] == 0:
            magic.popleft()
        continue

    total = materials[-1] * magic[0]
    if total in need:
        for key, value in presents.items():
            if total == value['need']:
                value['count'] += 1
                materials.pop()
                magic.popleft()
    elif total < 0:
        sum_total = materials[-1] + magic[0]
        magic.popleft()
        materials[-1] = sum_total
    elif total > 0:
        magic.popleft()
        materials[-1] += 15

if (presents['Doll']['count'] and presents['Wooden train']['count']) or (presents['Teddy bear']['count']
                                                                         and presents['Bicycle']['count']):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join(list(str(x) for x in materials)[::-1])}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")
for key, value in sorted(presents.items()):
    if value:
        print(f"{key}: {value['count']}")



