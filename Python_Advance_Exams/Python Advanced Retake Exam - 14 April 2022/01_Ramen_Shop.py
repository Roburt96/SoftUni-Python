from collections import deque

bowls_of_ramen = deque(int(x) for x in input().split(', '))
customers = deque(int(x) for x in input().split(', '))


while bowls_of_ramen and customers:
    ramen = bowls_of_ramen.pop()
    client = customers.popleft()

    if ramen == client:
        continue

    if ramen > client:
        ramen -= client
        bowls_of_ramen.append(ramen)

    elif ramen < client:
        client -= ramen
        customers.appendleft(client)

if len(customers) == 0:
    print(f"Great job! You served all the customers.")
    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls_of_ramen)}")

elif len(customers) > 0:
    print(f"Out of ramen! You didn't manage to serve all customers.")
    if customers:
        print(f"Customers left: {', '.join(str(x) for x in customers)}")
