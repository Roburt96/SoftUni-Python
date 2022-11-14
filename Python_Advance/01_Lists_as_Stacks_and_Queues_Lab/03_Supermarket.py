from collections import deque

queue = deque()
while True:
    cmd = input()
    if cmd == "Paid":
        while len(queue):
            print(queue.popleft())
    elif cmd == "End":
        print(f"{len(queue)} people remaining.")
        break
    else:
        queue.append(cmd)


