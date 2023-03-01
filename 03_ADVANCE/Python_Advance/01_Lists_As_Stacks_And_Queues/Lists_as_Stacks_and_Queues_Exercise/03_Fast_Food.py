from collections import deque  # not ok

quantity_of_food = int(input())
quantity_each_order = deque([int(x) for x in input().split()])
max_order = max(quantity_each_order)


for i in range(len(quantity_each_order)):
    current = quantity_each_order[0]
    if len(quantity_each_order) > 0:
        if quantity_of_food >= current:
            quantity_of_food -= quantity_each_order.popleft()
        elif quantity_of_food < current:
            break




print(max_order)
if not quantity_each_order:
    print("Orders complete")
elif quantity_each_order:
    quantity_each_order = [str(x) for x in quantity_each_order]
    print(f"Orders left: {' '.join(quantity_each_order)}")