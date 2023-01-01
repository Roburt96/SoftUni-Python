from collections import deque

chocolate = deque(int(x) for x in input().split(', '))   # pop
milk = deque(int(x) for x in input().split(', '))     # popleft
milkshake = 0


while chocolate and milk and milkshake != 5:
    if chocolate[-1] <= 0 and milk[0] <= 0:
        milk.popleft()
        chocolate.popleft()
        continue
    elif chocolate[-1] <= 0:
        chocolate.pop()
        continue
    elif milk[0] <= 0:
        milk.popleft()
        continue

    if chocolate[-1] == milk[0]:
        chocolate.pop()
        milk.popleft()
        milkshake += 1

    else:
        milk.append(milk.popleft())
        chocolate.append(chocolate.pop() - 5)


if milkshake == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate:
    print(f"Chocolate: {', '.join(str(x) for x in chocolate)}")
else:
    print("Chocolate: empty")

if milk:
    print(f"Milk: {', '.join(str(x) for x in milk)}")
else:
    print("Milk: empty")


