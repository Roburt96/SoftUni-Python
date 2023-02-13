# move = {
#     'left': {'row': 0, 'col': -1},
#     'right': {'row': 0, 'col': 1},
#     'up': {'row': -1, 'col': 0},
#     'down': {'row': 1, 'col': 0}
# }
#
# size = int(input())
# p_row, p_col = 0, 0
# matrix = []
# coins = 0
# path  = []
# win = False
#
# for row in range(size):
#     matrix.append([int(x) if x.isdigit() else x for x in input().split()])
#     if "P" in matrix[row]:
#         p_row, p_col = row, matrix[row].index('P')
#         path.append([p_row, p_col])
#         matrix[p_row][p_col] = '.'
#
#
# while True:
#     move_command = input()
#
#     if move[move_command]:
#         p_row, p_col = p_row + move[move_command]['row'], p_col + move[move_command]['col']
#
#         if p_row < 0:
#             p_row = size - 1
#         if p_row > size - 1:
#             p_row = 0
#         if p_col < 0:
#             p_col = size - 1
#         if p_col > size - 1:
#             p_col = 0
#         path.append([p_row, p_col])
#         if matrix[p_row][p_col] == "X":
#             coins = round(coins * 0.5)
#             break
#
#         elif matrix[p_row][p_col] == ".":
#             continue
#
#         else:
#             coins += matrix[p_row][p_col]
#             matrix[p_row][p_col] = "."
#
#     if coins >= 100:
#         win = True
#         break
#
#


class CollectingCoins:

    def __init__(self):
        self.size = int(input())
        self.matrix = []
        self.row = 0
        self.col = 0
        self.collected_coins = 0
        self.path = []
        self.win = False
        self.main()

    def main(self):
        self.make_matrix()
        self.main_loop()

    def make_matrix(self):
        for row in range(self.size):
            self.matrix.append(int(x) if x.isdigit() else x for x in input().split(','))
            if 'P' in self.matrix[row]:
                self.row, self.col = row, self.matrix[row].index('P')
                self.path.append([self.row, self.col])
                self.matrix[self.row][self.col] = '.'

    def main_loop(self):
        while True:
            cur_move = input()

            if cur_move == 'up':
                self.row -= 1

            elif cur_move == 'down':
                self.row += 1

            elif cur_move == 'left':
                self.col -= 1

            elif cur_move == 'right':
                self.col += 1

            if self.row >= self.size:
                self.row = 0
            elif self.row < 0 :
                self.row = self.size - 1

            if self.col >= self.size:
                self.col = 0
            elif self.col < 0 :
                self.col = self.size - 1

            if self.matrix[self.row][self.col] == 'X':
                self.collected_coins /= 2
                break

            elif self.matrix[self.row][self.col] == ".":
                continue

            else:
                self.collected_coins += self.matrix[self.row][self.col]
                self.path.append([self.row, self.col])
                self.matrix[self.row][self.col] = '.'

            if self.collected_coins >= 100:
                self.win = True
                break

        if not self.win:
            print(f"Game over! You've collected {round(self.collected_coins)} coins.")
        else:
            print(f"You won! You've collected {round(self.collected_coins)} coins.")
        print('Your path:')
        print('\n'.join(str(x) for x in self.path))


if __name__ == '__main__':
    CollectingCoins()



