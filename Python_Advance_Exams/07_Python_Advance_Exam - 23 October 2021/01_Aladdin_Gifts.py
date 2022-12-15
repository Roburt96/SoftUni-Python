from collections import deque

materials = deque(int(x) for x in input().split())
magic_level = deque(int(x) for x in input().split())

magic_items = {
    'Gemstone': {'low': 100, 'high': 199, 'count': 0},
    'Porcelain Sculpture': {'low': 200, 'high': 299, 'count': 0},
    'Gold': {'low': 200, 'high': 299, 'count': 0},
    'Diamon Jewellery': {'low': 300, 'high': 499, 'count': 0}

}


def craft_(total):
    for key, value in magic_items.items():
        if value['low'] <= total <= value['high']:
            magic_items[key]['count'] += 1
            return


def check_pairs():
    if magic_items['Gemstone']['count'] > 0 and magic_items['Porcelain Sculpture']['count'] > 0:
        return True
    elif magic_items['Gold']['count'] > 0 and magic_items['Diamon Jewellery']['count'] > 0:
        return True


while materials and magic_level:

    current_material = materials.pop()
    current_magic = magic_level.popleft()
    total_current = current_material + current_magic

    if 100 <= total_current <= 499:
        craft_(total_current)
        continue

    if total_current < 100:
        if total_current % 2 == 0:
            current_material *= 2
            current_magic *= 3
            total_current = current_material + current_magic
            craft_(total_current)
        else:
            current_material *= 2
            current_magic *= 3
            total_current = current_material + current_magic
            craft_(total_current)

    elif total_current > 499:
        current_material /= 2
        current_magic /= 2
        total_current = current_material + current_magic
        craft_(total_current)


if check_pairs():
    print('The wedding presents are made!')
else:
    print('Aladdin does not have enough wedding presents.')

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")

if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")

for key, value in sorted(magic_items.items()):
    if value['count'] > 0:
        print(f"{key}: {value['count']}")