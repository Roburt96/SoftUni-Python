position = ((-2, -1), #up left
            (-2, 1), #up right
            (-1, -2), # left up
            (-1, 2), # right up
            (1, -2), # left down
            (1, 2), # right down
            (2, -1), # down left
            (2, 1)) # down right


class KnightGame:
    position = (
        (-2, -1),  # up left
        (-2, 1),  # up right
        (-1, -2),  # left up
        (-1, 2),  # right up
        (1, -2),  # left down
        (1, 2),  # right down
        (2, -1),  # down left
        (2, 1))  # down right

    def __init__(self):
        self.size = int(input())
        self.matrix_table = [[x for x in input()]for _ in range(self.size)]
        self.hits = 0
        self.removed = 0
        self.removed_horse = []
        self.main_func()


    def main_func(self):
        self.check_hits()

    # def hits(self, matrix, row, col):
    #     if matrix[row][col] == 'K'
    #

    def check_hits(self):
        while True:
            max_hits = 0
            for row in range(len(self.matrix_table)):
                for col in range(len(self.matrix_table)):
                    if self.matrix_table[row][col] == 'K':
                        current_horse = [row, col]
                        for move in KnightGame.position:
                            horse_row = row + move[0]
                            horse_col = col + move[1]
                            if 0 <= horse_row < self.size and 0 <= horse_col < self.size:
                                if self.matrix_table[horse_row][horse_col] == 'K':
                                    self.hits += 1
                        if self.hits > max_hits:
                            max_hits = max_hits
                            self.removed_horse = current_horse
            if max_hits > 0:
                self.matrix_table[self.removed_horse[0]][self.removed_horse[1]] = '0'
                self.removed += 1
            else:
                break
        print(self.removed)

knight = KnightGame()




