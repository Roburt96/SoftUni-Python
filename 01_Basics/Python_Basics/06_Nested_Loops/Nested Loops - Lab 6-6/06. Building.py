floors = int(input())
rooms = int(input())

for floor in range(floors, 0, -1):
    for room in range(0, rooms):
        if floor == floors:
            print(f"L{floor}{room}", end =" ")
        elif floor % 2 == 0:
            print(f"O{floor}{room}", end=" ")
        elif floor % 2 != 0:
            print(f"A{floor}{room}", end=" ")
    print()
