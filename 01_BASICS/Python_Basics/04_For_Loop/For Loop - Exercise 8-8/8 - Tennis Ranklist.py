import math

tournaments = int(input())
starting_points = int(input())

tournament = 1
points = starting_points
average_points = 0
win_counter = 0

for tournament in range(tournaments):
    result = input()
    if result == "W":
        points += 2000
        average_points += 2000
        win_counter += 1
        tournament += 1
    elif result == "SF":
        points += 720
        average_points += 720
        tournament += 1
    elif result == "F":
        points += 1200
        average_points += 1200
        tournament += 1


percentage_won = win_counter / tournaments * 100

print(f'Final points: {points}')
print(f'Average points: {math.floor(average_points / tournaments)}')
print(f'{percentage_won:.2f}%')
