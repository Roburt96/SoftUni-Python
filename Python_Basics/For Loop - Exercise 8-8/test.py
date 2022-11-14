import math

number_tournaments = int(input())
starting_ranklist_points = int(input())
all_points = 0
win_counter = 0
average_points = 0
average_win = 0

for points in range(number_tournaments):
    result = input()
    if result == "W":
        points += 2000
        win_counter += 1
    elif result == "SF":
        points += 720
    elif result == "F":
        points += 1200

    starting_ranklist_points += points
    average_points += points // number_tournaments
average_win = win_counter / number_tournaments * 100

print(f"Final points: {starting_ranklist_points}")
print(f"Average points: {math.floor(average_points)}")
print(F"{average_win:.2f}%")