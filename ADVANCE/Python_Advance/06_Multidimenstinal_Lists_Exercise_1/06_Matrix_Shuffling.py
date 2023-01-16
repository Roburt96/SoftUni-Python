row, col = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()]for _ in range(row)]

command = input()

while command != "END":
    cmd, *data = [int(x) if x.isdigit() else x for x in command.split()]
    if cmd != 'swap' or len(data) != 4 or any([True for x in data if x < 0 or x > len(matrix)]):
        print("Invalid input!")

    if cmd == 'swap':
        first_row, first_col = data[0], data[1]
        second_row, second_col = data[2], data[3]
        matrix[first_row][first_col], matrix[second_row][second_col] = \
            matrix[second_row][second_col], matrix[first_row][first_col]
        for row in range(len(matrix)):
            print(*matrix[row], sep=" ")



    command = input()