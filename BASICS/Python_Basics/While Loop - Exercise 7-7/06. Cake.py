width = int(input())
height = int(input())

total_pieces = width * height


command = input()
while command != "STOP":
    pieces = int(command)
    total_pieces -= pieces

    if total_pieces < 0:
        break

    command = input()

diff = abs(total_pieces)

if total_pieces >= 0:
    print(f"{diff} pieces are left.")
else:
    print(f"No more cake left! You need {diff} pieces more.")
