from collections import deque


working_bees = deque(int(x) for x in input().split()) #popleft
nectars = deque(int(x) for x in input().split())   # pop
symbols = deque(input().split())
total_honey = 0


while working_bees and nectars:
    bee = working_bees.popleft()
    nectar = nectars.pop()

    if bee > nectar:
        working_bees.appendleft(bee)
        continue
    operation = symbols.popleft()
    if nectar > 0:
        if operation == "+":
            total_honey += abs(bee + nectar)
        elif operation == "-":
            total_honey += abs(bee - nectar)
        elif operation == "*":
            total_honey += abs(bee * nectar)
        elif operation == "/":
            total_honey += abs(bee / nectar)
print(f"Total honey made: {total_honey}")

if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if nectars:
    print(f"Nectar left: {', '.join(str(x) for x in nectars)}")


