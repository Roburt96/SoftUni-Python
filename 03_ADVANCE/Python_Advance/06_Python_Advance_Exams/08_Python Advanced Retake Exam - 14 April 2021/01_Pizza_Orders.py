from collections import deque

pizza_orders = deque(int(x) for x in input().split(', '))
employees_capacities = deque(int(x) for x in input().split(', '))

completed = 0

while pizza_orders and employees_capacities:
    if pizza_orders[0] <= 0:
        pizza_orders.popleft()
        continue

    if pizza_orders[0] > 10:
        pizza_orders.popleft()
        continue

    current_pizza = pizza_orders.popleft()
    current_employee = employees_capacities.pop()

    if current_pizza <= current_employee:
        completed += current_pizza

    elif current_pizza > current_employee:
        pizza_left = current_pizza - current_employee
        completed += current_pizza - pizza_left
        pizza_orders.appendleft(pizza_left)


if not pizza_orders:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {completed}')
    print(f"Employees: {', '.join(str(x) for x in employees_capacities)}")

else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in pizza_orders)}")