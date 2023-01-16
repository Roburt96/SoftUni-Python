rows = int(input())
matrix = [[int(x) for x in input().split()]for _ in range(rows)]

END_LOOP = "END"

command = input()
while command != END_LOOP:
    cmd_type, *data = [x for x in command.split()]
    row = int(data[0])
    col = int(data[1])
    value = int(data[2])

    if cmd_type == "Add":
        if 0 <= row < len(matrix) and 0 <= col < len(matrix):
            matrix[row][col] += value
        else:
            print("Invalid coordinates")

    elif cmd_type == "Subtract":
        if 0 <= row < len(matrix) and 0 <= col < len(matrix):
            matrix[row][col] -= value
        else:
            print("Invalid coordinates")

    command = input()

[print(*matrix[row]) for row in range(rows)]
