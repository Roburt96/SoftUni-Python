
needed = {
    'Water deposit': 0,
    'Metal deposit': 0,
    'Concrete deposit': 0
}
matrix = []
row, col = 0, 0


for rows in range(6):
    matrix.append(input().split())
    if "E" in matrix[rows]:
        row, col = rows, matrix[rows].index("E")

cmds = [x for x in input().split(", ")]

for i in range(len(cmds)):

    if cmds[i] == "up":
        row -= 1
    elif cmds[i] == "down":
        row += 1
    elif cmds[i] == "left":
        col -= 1
    elif cmds[i] == "right":
        col += 1

    if 0 > row:
        row = 5
    if 0 > col:
        col = 5

    if matrix[row][col] == "W":
        needed['Water deposit'] += 1
        print(f"Water deposit found at ({row}, {col})")

    elif matrix[row][col] == "M":
        needed['Metal deposit'] += 1
        print(f"Metal deposit found at ({row}, {col})")

    elif matrix[row][col] == "C":
        needed['Concrete deposit'] += 1
        print(f"Concrete deposit found at ({row}, {col})")

    elif matrix[row][col] == "R":
        print(f"Rover got broken at ({row}, {col})")
        break

if needed['Water deposit'] > 0 and needed['Metal deposit'] > 0 and needed['Concrete deposit'] > 0:
    print("Area suitable to start the colony.")

else:
    print("Area not suitable to start the colony.")











