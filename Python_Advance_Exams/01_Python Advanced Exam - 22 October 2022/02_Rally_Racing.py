directions = {
    'up': {'row': -1, 'col': 0},
    'down': {'row': 1, 'col': 0},
    'left': {'row': 0, 'col': -1},
    'right': {'row': 0, 'col': 1}
}

matrix_size = int(input())
racing_number = int(input())
km = 0
car_row, car_col = 0, 0
matrix, tunnels = [], []

for row_ in range(matrix_size):
    matrix.append(input().split())

    if "T" in matrix[row_]:
        tunnels.append([row_, matrix[row_].index('T')])

command = input()
while command != 'End':
    car_row, car_col = car_row + directions[command]['row'], car_col + directions[command]['col']
    current = matrix[car_row][car_col]

    if current == ".":
        km += 10

    elif current == "T":
        km += 30
        matrix[car_row][car_col] = "."
        tunnels.remove([car_row, car_col])
        car_row, car_col = tunnels[0]
        matrix[car_row][car_col] = "."

    elif current == "F":
        km += 10
        print(f"Racing car {racing_number} finished the stage!")
        break

    command = input()
else:
    print(f"Racing car {racing_number} DNF.")

matrix[car_row][car_col] = "C"
print(f"Distance covered {km} km.")
[print(*row, sep="") for row in matrix]




