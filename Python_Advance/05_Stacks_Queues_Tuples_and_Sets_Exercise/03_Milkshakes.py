from collections import deque

chocolate = deque(int(x) for x in input().split(', '))   # pop
milk = deque(int(x) for x in input().split(', '))     # popleft
milkshake = 0
target = False

while chocolate and milk:
    if chocolate[-1] < 0:
        chocolate.pop()
        continue
    if milk[0] < 0:
        milk.popleft()
        continue

    if chocolate[-1] == milk[0]:
        chocolate.pop()
        milk.popleft()
        milkshake += 1

    else:
        milk.append(milk.popleft())
        chocolate.appendleft(chocolate.pop() - 5)


    if milkshake == 5:
        target = True
        break

if target:
    print("Great! You made all the chocolate milkshakes needed!")

if chocolate:
    print(f"Chocolate: {', '.join(str(x) for x in chocolate)}")
else:
    print("Chocolate: empty")
if milk:
    print(f"Milk: {', '.join(str(x) for x in milk)}")
else:
    print("Milk empty")


