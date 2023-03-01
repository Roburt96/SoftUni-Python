# row, col = [int(x) for x in input().split(", ")]
# matrix = []
# cur_row, cur_col = 0, 0
#
# items = {
#     'Gifts': 0,
#     'Cookies': 0,
#     'Christmas decorations': 0
# }
#
# for rows in range(row):
#     matrix.append(input().split())
#     if "Y" in matrix[rows]:
#         cur_row, cur_col = rows, matrix[rows].index("Y")
#
# def check_items():
#     result = 0
#     for r in range(row):
#         for c in range(col):
#             if matrix[r][c] != "." and matrix[r][c] != 'x' and matrix[r][c] != 'Y':
#                 result += 1
#
# command = input()
# while command != 'End':
#     cmd, steps = [int(x) if x.isdigit() else x for x in command.split("-")]
#
#     while steps > 0:
#         santa_row, santa_col = cur_row, cur_col
#         matrix[santa_row][santa_col] = 'x'
#         if cmd == "right":
#             santa_col += 1
#         elif cmd == "left":
#             santa_col -= 1
#         elif cmd == "up":
#             santa_row -= 1
#         elif cmd == "down":
#             santa_row += 1
#         steps -= 1
#         if santa_row > row:
#             santa_row = 0
#         if santa_row < 0:
#             santa_row = 5
#         if santa_col > col:
#             santa_col = 0
#         if santa_col < 0:
#             santa_col = 4
#
#         if matrix[santa_row][santa_col] == "D":
#             items['Christmas decorations'] += 1
#             matrix[santa_row][santa_col] = "x"
#         elif matrix[santa_row][santa_col] == "G":
#             items['Gifts'] += 1
#             matrix[santa_row][santa_col] = "x"
#         elif matrix[santa_row][santa_col] == "C":
#             items['Cookies'] += 1
#             matrix[santa_row][santa_col] = "C"
#         elif matrix[santa_row][santa_col] == ".":
#             matrix[santa_row][santa_col] = 'x'
#         elif matrix[santa_row][santa_col] == 'x':
#             pass
#
#         cur_row, cur_col = santa_row, santa_col
#         [print(*row) for row in matrix]
#
#     matrix[cur_row][cur_col] = 'Y'
#     print()
#     print()
#     [print(*row) for row in matrix]
#
#     command = input()


class NorthPoleChallenge:

    def __init__(self):
        self.row, self.col = [int(x) for x in input().split(", ")]
        self.matrix = []
        self.santa_row, self.santa_col = 0, 0
        self.items = {
            'Christmas decorations': 0,
            'Gifts': 0,
            'Cookies': 0
        }
        self.all_gifts = 0
        self.collect_all = False
        self.main()

    def main(self):
        self.make_matrix()
        self.check_items()
        self.loop_matrix()

    def make_matrix(self):
        for r in range(self.row):
            self.matrix.append(input().split())
            if "Y" in self.matrix[r]:
                self.santa_row, self.santa_col = r, self.matrix[r].index("Y")

    def check_items(self):
        for r in range(self.row):
            for c in range(self.col):
                if self.matrix[r][c] != "." and self.matrix[r][c] != 'x' and self.matrix[r][c] != 'Y':
                    self.all_gifts += 1

    def loop_matrix(self):
        while self.all_gifts:
            command = input().split("-")
            if command[0] == "End":
                break

            cmd, steps = command[0], int(command[1])

            for _ in range(steps):
                cur_row, cur_col = self.santa_row, self.santa_col
                self.matrix[cur_row][cur_col] = 'x'
                steps -= 1

                if cmd == "right":
                    cur_col += 1
                elif cmd == "left":
                    cur_col -= 1
                elif cmd == "up":
                    cur_row -= 1
                elif cmd == "down":
                    cur_row += 1

                if cur_row > self.row:
                    cur_row = 0
                if cur_row < 0:
                    cur_row = self.row - 1
                if cur_col > self.col:
                    cur_col = 0
                if cur_col < 0:
                    cur_col = self.col - 1

                if self.matrix[cur_row][cur_col] == "D":
                    self.items['Christmas decorations'] += 1
                    self.matrix[cur_row][cur_col] = "x"
                    self.all_gifts -= 1

                elif self.matrix[cur_row][cur_col] == "G":
                    self.items['Gifts'] += 1
                    self.matrix[cur_row][cur_col] = "x"
                    self.all_gifts -= 1

                elif self.matrix[cur_row][cur_col] == "C":
                    self.items['Cookies'] += 1
                    self.matrix[cur_row][cur_col] = "x"
                    self.all_gifts -= 1

                elif self.matrix[cur_row][cur_col] == ".":
                    self.matrix[cur_row][cur_col] = 'x'

                elif self.matrix[cur_row][cur_col] == 'x':
                    continue

                if self.all_gifts == 0:
                    print("Merry Christmas!")
                    self.collect_all = True
                    self.matrix[cur_row][cur_col] = 'Y'
                    break

                self.santa_row, self.santa_col = cur_row, cur_col
                self.matrix[cur_row][cur_col] = 'Y'


        if self.collect_all:
            print("You've collected:")
            for key, value in self.items.items():
                print(f"- {key} {value}")
            [print(*row) for row in self.matrix]
        else:
            print("You've collected:")
            for key, value in self.items.items():
                print(f"- {key} {value}")
            [print(*row) for row in self.matrix]


if __name__ == '__main__':
    NorthPoleChallenge()





