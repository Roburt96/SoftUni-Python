from collections import deque

bomb = deque(int(x) for x in input().split(', '))   # popleft
casings = deque(int(x) for x in input().split(', '))    # pop

bomb_type = {
    'Datura Bombs': {'need': 40, 'counter': 0},
    'Cherry Bombs': {'need': 60, 'counter': 0},
    'Smoke Decoy Bombs': {'need': 120, 'counter': 0}
}

# def check_bomb(current):
#     for key, value in bomb_type.items():
#         if current == value['need']:
#             bomb_type[key]['counter'] += 1
#             return
#         return

while bomb and casings:

    if len(bomb) == 0:
        break
    if len(casings) == 0:
        break
    if bomb[0] <= 0:
        bomb.popleft()
    if casings[-1] <= 0:
        casings.pop()
    if bomb_type['Datura Bombs']['counter'] >= 3 and bomb_type['Cherry Bombs']['counter'] >= 3 and \
            bomb_type['Smoke Decoy Bombs']['counter'] >= 3:
        break

    current_bomb = bomb.pop()
    current_casings = casings.popleft()
    total = current_bomb + current_casings
    if total == 40:
        bomb_type['Datura Bombs']['counter'] += 1
        continue
    if total == 60:
        bomb_type['Cherry Bombs']['counter'] += 1
        continue
    if total == 120:
        bomb_type['Smoke Decoy Bombs']['counter'] += 1
        continue

    if total != 40 and total != 60 and total != 120:
        bomb.append(current_bomb)
        casings.append(current_casings - 5)
        continue


all_bombs = 0
for key, value in bomb_type.items():
    if value['counter'] > 0:
        all_bombs += 1

if all_bombs >= 3:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb)}")
elif not bomb:
    print("Bomb Effects: empty")

if casings:
    print(f"Bomb Casings: {', '.join(str(x) for x in casings)}")
elif not casings:
    print("Bomb Casings: empty")

for key, value in sorted(bomb_type.items(), key=lambda x: x[0]):
    print(f"{key}: {value['counter']}")