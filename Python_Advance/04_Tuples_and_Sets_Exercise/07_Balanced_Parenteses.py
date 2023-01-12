from collections import deque

parentheses = deque(input())
open_bracket = deque()
balanced = True
while parentheses:
    current_bracket = parentheses.popleft()
    if current_bracket in "{[(":
        open_bracket.append(current_bracket)
    elif not open_bracket:
        balanced = False
        break
    else:
        if f"{open_bracket.pop() + current_bracket}" not in "{}()[]":
            balanced = False
            break

if balanced and not open_bracket:
    print("YES")
else:
    print("NO")