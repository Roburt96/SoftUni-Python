from collections import deque
kids, potato_move= input().split(), int(input())
queue = deque(kids)
while len(queue) != 1:
    queue.rotate(-potato_move)
    print(f"Removed {queue.pop()}")
print(f"Last is {''.join(queue)}")


