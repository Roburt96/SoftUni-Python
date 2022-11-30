box_of_clothes = [int(number) for number in input().split()]
capacity_one_rack = int(input())
racks = []
total_racks = 0
for cloth in range(len(box_of_clothes) - 1, -1, -1):
    current_cloth = box_of_clothes.pop()
    racks.append(current_cloth)
    if sum(racks) == capacity_one_rack:
        if box_of_clothes:
            racks = []
            total_racks += 1
    elif sum(racks) > capacity_one_rack:
        racks = [current_cloth]
        total_racks += 1
if racks:
    total_racks += 1

print(total_racks)
