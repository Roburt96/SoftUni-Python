first_game = input()
second_game = input()
third_game = input()

win = 0
lost = 0
drawn = 0

if ord(first_game[0]) > ord(first_game[2]):
    win += 1
elif ord(first_game[0]) < ord(first_game[2]):
    lost += 1
else:
    drawn += 1

if ord(second_game[0]) > ord(second_game[2]):
    win += 1
elif ord(second_game[0]) < ord(second_game[2]):
    lost += 1
else:
    drawn += 1

if ord(third_game[0]) > ord(third_game[2]):
     win += 1
elif ord(third_game[0]) < ord(third_game[2]):
     lost += 1
else:
    drawn += 1

print(f"Team won {win} games.")
print(f"Team lost {lost} games.")
print(f"Drawn games: {drawn}")
