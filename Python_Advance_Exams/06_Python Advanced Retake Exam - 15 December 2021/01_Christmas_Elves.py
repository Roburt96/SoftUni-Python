from collections import deque

elf_energy = deque(int(x) for x in input().split())
materials = deque(int(x) for x in input().split())
toys_counter = 0
try_to_create = 0
total_energy = 0

while elf_energy and materials:
    while elf_energy[0] < 5:
        if len(elf_energy) == 0:
            break
    if len(elf_energy) == 0:
        break
    current_elf = elf_energy.popleft()
    current_material = materials.pop()
    try_to_create += 1

    if try_to_create % 3 == 0:
        double_material = current_material * 2
        if current_elf >= double_material:
            toys_counter += 2
            current_elf -= double_material
            current_elf += 1
            total_energy += current_material
            elf_energy.append(current_elf)
            materials.appendleft(current_material)
        else:
            current_elf *= 2
            elf_energy.append(current_elf)
            continue
    if try_to_create % 5 == 0:
        if current_elf >= current_material:
            current_elf -= current_material
            if current_elf > 0:
                elf_energy.append(current_elf)
                continue

    if current_elf >= current_material:
        toys_counter += 1
        current_elf -= current_material
        total_energy += current_material
        current_elf += 1
        elf_energy.append(current_elf)

print(f"Toys: {toys_counter}")
print(f"Energy: {total_energy}")

if elf_energy:
    print(f"Elves left: {', '.join(str(x) for x in elf_energy)}")
if materials:
    print(f"Boxes left: {', '.join(str(x) for x in materials)}")
