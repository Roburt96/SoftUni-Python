from collections import deque

eggs_size = deque(int(x) for x in input().split(', '))
paper_size = deque(int(x) for x in input().split(', '))
box_size = 50
filled_box = 0

while eggs_size and paper_size:
    current_egg = eggs_size.popleft()

    if current_egg <= 0:
        continue

    if current_egg == 13:
        paper_size[0], paper_size[-1] = paper_size[-1], paper_size[0]
        continue

    current_paper = paper_size.pop()
    total = current_paper + current_egg
    if total <= box_size:
        filled_box += 1


if filled_box:
    print(f"Great! You filled {filled_box} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")

if eggs_size:
    print(f"Eggs left: {', '.join(str(x) for x in eggs_size)}")
if paper_size:
    print(f"Pieces of paper left: {', '.join(str(x) for x in paper_size)}")


