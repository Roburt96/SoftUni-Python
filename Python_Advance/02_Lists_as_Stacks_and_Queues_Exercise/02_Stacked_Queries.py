from collections import deque

stack = deque()
num_of_cmd = int(input())
final_stack = []
for i in range(num_of_cmd):
    cmd, *num = [int(x) for x in input().split()]
    if cmd == 1:
        stack.append(num[0])
    elif cmd == 2:
        if len(stack) != 0:
            stack.pop()
    elif cmd == 3:
        print(max(stack))
    elif cmd == 4:
        print(min(stack))

for i in range(len(stack)):
    final_stack.append(stack.pop())
print(*final_stack, sep=", ")
