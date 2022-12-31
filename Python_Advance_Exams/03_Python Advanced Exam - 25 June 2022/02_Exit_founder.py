
players = [{"name": x, "rest": False} for x in input().split(", ")]
matrix = [[x for x in input().split()]for _ in range(6)]

while True:
    cur_row, cur_col = [int(x) for x in input()[1:-1].split(", ")]
    player = players.pop(0)
    winner = players.pop(0)
    move_to = matrix[cur_row][cur_col]

    if player['rest']:
        player['rest'] = False

    elif move_to == "E":
        print(f"{player['name']} found the Exit and wins the game!")
        break

    elif move_to == "T":
        print(f"{player['name']} is out of the game! The winner is {winner['name']}.")
        break

    elif move_to == "W":
        print(f"{player['name']} hits a wall and needs to rest.")

    players.append(winner)
    players.append(player)

