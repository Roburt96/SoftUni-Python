from collections import deque

materials = [int(x) for x in input().split()]
magics = deque(int(x) for x in input().split())

presents = {
    "Bicycle": [0, 400],
    "Doll": [0, 150],
    "Teddy bear": [0, 300],
    "Wooden train": [0, 250]
}

while materials and magics:
    cur_material = materials.pop()
    cur_magic = magics.popleft()

    if cur_material == 0 and cur_magic == 0:
        continue
    if cur_material == 0:
        magics.appendleft(cur_magic)
        continue
    if cur_magic == 0:
        materials.append(cur_material)
        continue

    product_of_operation = cur_material * cur_magic
    if product_of_operation < 0:
        result = cur_material + cur_magic
        materials.append(result)

    else:
        found_present = False
        for gift, data in presents.items():
            amount, magic_level = data
            if magic_level == product_of_operation:
                presents[gift][0] += 1
                found_present = True
                break
        if product_of_operation > 0 and not found_present:
            materials.append(cur_material + 15)

if (presents["Bicycle"][0] >= 1 and presents["Teddy bear"][0] >= 1) or \
        (presents["Doll"][0] >= 1 and presents["Wooden train"][0] >= 1):
    print(f"The presents are crafted! Merry Christmas!")
else:
    print(f"No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials[::-1])}")

if magics:
    print(f"Magic left: {', '.join(str(x) for x in magics)}")

for gift, data in presents.items():
    amount, pts = data
    if amount >= 1:
        print(f"{gift}: {amount}")



