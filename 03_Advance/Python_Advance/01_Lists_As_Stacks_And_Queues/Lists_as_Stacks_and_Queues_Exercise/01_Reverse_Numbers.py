from collections import deque

strings = deque([int(x) for x in input().split()])
new_strings = []
for i in range(len(strings)):
    new_strings.append(strings.pop())
print(*new_strings)