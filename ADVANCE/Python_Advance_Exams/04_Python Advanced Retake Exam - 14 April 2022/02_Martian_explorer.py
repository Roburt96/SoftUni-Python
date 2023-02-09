# needed = {
#     'Water deposit': 0,
#     'Metal deposit': 0,
#     'Concrete deposit': 0
# }
# matrix = []
# row, col = 0, 0
#
#
# for rows in range(6):
#     matrix.append(input().split())
#     if "E" in matrix[rows]:
#         row, col = rows, matrix[rows].index("E")
#
# cmds = [x for x in input().split(", ")]
#
# for i in range(len(cmds)):
#
#     if cmds[i] == "up":
#         row -= 1
#     elif cmds[i] == "down":
#         row += 1
#     elif cmds[i] == "left":
#         col -= 1
#     elif cmds[i] == "right":
#         col += 1
#
#     if 0 > row:
#         row = 5
#     if 0 > col:
#         col = 5
#
#     if matrix[row][col] == "W":
#         needed['Water deposit'] += 1
#         print(f"Water deposit found at ({row}, {col})")
#
#     elif matrix[row][col] == "M":
#         needed['Metal deposit'] += 1
#         print(f"Metal deposit found at ({row}, {col})")
#
#     elif matrix[row][col] == "C":
#         needed['Concrete deposit'] += 1
#         print(f"Concrete deposit found at ({row}, {col})")
#
#     elif matrix[row][col] == "R":
#         print(f"Rover got broken at ({row}, {col})")
#         break
#
# if needed['Water deposit'] > 0 and needed['Metal deposit'] > 0 and needed['Concrete deposit'] > 0:
#     print("Area suitable to start the colony.")
#
# else:
#     print("Area not suitable to start the colony.")

class MartianExplorer:

    def __init__(self, row: int, col: int, matrix: list):
        self.needed = {
            'Water Deposit': 0,
            'Metal Deposit': 0,
            'Concrete Deposit': 0
        }
        self.position = {
            'up': {'row': -1, 'col': 0},
            'down': {'row': 1, 'col': 0},
            'left': {'row': 0, 'col': -1},
            'right': {'row': 0, 'col': 1}
        }
        self.matrix = matrix
        self.row = row
        self.col = col
        self.commands = []
        self.main()

    def main(self):
        self.append_commands()
        self.find_resources()

    def append_commands(self):
        self.commands = input().split(', ')

    def find_resources(self):
        for cmd in range(len(self.commands)):
            if self.commands[cmd] == 'up':
                self.row -= 1

            elif self.commands[cmd] == 'down':
                self.row += 1

            elif self.commands[cmd] == 'left':
                self.col -= 1

            elif self.commands[cmd] == 'right':
                self.col += 1

            if 0 > self.row:
                self.row = 0
            if 0 > self.col:
                self.col = 0

            if self.matrix[self.row][self.col] == 'W':
                self.needed['Water Deposit'] += 1
                print(f"Water deposit found at ({self.row}, {self.col})")

            elif self.matrix[self.row][self.col] == 'M':
                self.needed['Metal Deposit'] += 1
                print(f"Metal deposit found at ({self.row}, {self.col})")

            elif self.matrix[self.row][self.col] == 'C':
                self.needed['Concrete Deposit'] += 1
                print(f"Concrete deposit found at ({self.row}, {self.col})")

            elif self.matrix[self.row][self.col] == 'R':
                print(f"Rover got broken at ({self.row}, {self.col})")
                break

        if self.needed['Water Deposit'] > 0 and self.needed['Metal Deposit'] > 0 and \
            self.needed['Concrete Deposit'] > 0:
            print("Area suitable to start the colony.")
        else:
            print("Area not suitable to start the colony.")


matrix = []
row, col = 0, 0


def make_matrix():
    global row
    global col
    for rows in range(6):
        matrix.append(input().split())
        if 'E' in matrix[rows]:
            row, col = rows, matrix[rows].index('E')


make_matrix()
MartianExplorer(row, col, matrix)














