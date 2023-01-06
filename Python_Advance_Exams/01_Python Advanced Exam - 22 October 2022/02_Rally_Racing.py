# directions = {
#     'up': {'row': -1, 'col': 0},
#     'down': {'row': 1, 'col': 0},
#     'left': {'row': 0, 'col': -1},
#     'right': {'row': 0, 'col': 1}
# }
#
# matrix_size = int(input())
# racing_number = int(input())
# km = 0
# car_row, car_col = 0, 0
# matrix, tunnels = [], []
#
# for row_ in range(matrix_size):
#     matrix.append(input().split())
#
#     if "T" in matrix[row_]:
#         tunnels.append([row_, matrix[row_].index('T')])
#
# command = input()
# while command != 'End':
#     car_row, car_col = car_row + directions[command]['row'], car_col + directions[command]['col']
#     current = matrix[car_row][car_col]
#
#     if current == ".":
#         km += 10
#
#     elif current == "T":
#         km += 30
#         matrix[car_row][car_col] = "."
#         tunnels.remove([car_row, car_col])
#         car_row, car_col = tunnels[0]
#         matrix[car_row][car_col] = "."
#
#     elif current == "F":
#         km += 10
#         print(f"Racing car {racing_number} finished the stage!")
#         break
#
#     command = input()
# else:
#     print(f"Racing car {racing_number} DNF.")
#
# matrix[car_row][car_col] = "C"
# print(f"Distance covered {km} km.")
# [print(*row, sep="") for row in matrix]

directions = {
    'up': {'row': -1, 'col': 0},
    'down': {'row': 1, 'col': 0},
    'left': {'row': 0, 'col': -1},
    'right': {'row': 0, 'col': 1}
}


def make_matrix(size):
    global matrix, tunnels
    for i in range(size):
        matrix.append(input().split())
        if "T" in matrix[i]:
            tunnels.append([i, matrix[i].index("T")])


def current_pos(current_p):
    global km, car_row, car_col
    if current_p == ".":
        km += 10
    elif current_p == "T":
        km += 30
        matrix[car_row][car_col] = "."
        tunnels.remove([car_row, car_col])
        car_row, car_col = tunnels[0]
        matrix[car_row][car_col] = "."


if __name__ == '__main__':
    matrix_size = int(input())
    racing_number = int(input())
    km = 0
    car_row, car_col = 0, 0
    matrix, tunnels = [], []
    make_matrix(matrix_size)
    finish = False
    command = input()
    while command != "End":
        car_row, car_col = car_row + directions[command]['row'], car_col + directions[command]['col']
        current = matrix[car_row][car_col]

        if current == "F":
            km += 10
            print(f"Racing car {racing_number} finished the stage!")
            matrix[car_row][car_col] = "C"
            finish = True
            break
        current_pos(current)
        command = input()
    if not finish:
        matrix[car_row][car_col] = "C"
        print(f"Racing car {racing_number} DNF.")


    print(f"Distance covered {km} km.")
    [print(*row, sep="") for row in matrix]
