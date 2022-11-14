from collections import deque
kids = input().split()
potato_move = int(input())
queue = deque(kids)
while len(queue) != 1:
    queue.rotate(-potato_move)
    print(f"Removed {queue.pop()}")
print(f"Last is {''.join(queue)}")


