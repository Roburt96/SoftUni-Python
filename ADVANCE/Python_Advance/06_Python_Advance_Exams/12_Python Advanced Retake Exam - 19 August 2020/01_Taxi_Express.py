from collections import deque

customers = deque(int(x) for x in input().split(', '))     # popleft
taxis = deque(int(x) for x in input().split(', '))         # pop
total_time = 0

while customers and taxis:
    current_taxi = taxis.pop()
    current_customer = customers.popleft()

    if current_taxi >= current_customer:
        total_time += current_customer

    else:
        customers.appendleft(current_customer)


if not customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")

else:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")