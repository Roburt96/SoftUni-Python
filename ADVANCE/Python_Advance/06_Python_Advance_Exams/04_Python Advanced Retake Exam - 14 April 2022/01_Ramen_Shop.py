from collections import deque

class RamenShop:

    def __init__(self):
        self.bowls_of_ramen = deque(int(x) for x in input().split(", "))
        self.customers = deque(int(x) for x in input().split(", "))
        self.main()

    def main(self):
        while self.bowls_of_ramen and self.customers:

            current_ramen = self.bowls_of_ramen.pop()
            current_customer = self.customers.popleft()

            if current_ramen == current_customer:
                continue

            if current_ramen > current_customer:
                current_ramen -= current_customer
                self.bowls_of_ramen.append(current_ramen)

            elif current_ramen < current_customer:
                current_customer -= current_ramen
                self.customers.appendleft(current_customer)

        if len(self.customers) == 0:
            print(f"Great job! You server all the customers.")
            if self.bowls_of_ramen:
                print(f"Bowls of ramen left: {', '.join(str(x) for x in self.bowls_of_ramen)}")

        elif len(self.customers) > 0:
            print(f"Out of ramen! You didn't manage to serve all customers.")
            if self.customers:
                print(f"Customers left: {', '.join(str(x) for x in self.customers)}")



# bowls_of_ramen = deque(int(x) for x in input().split(', '))
# customers = deque(int(x) for x in input().split(', '))
#
#
# while bowls_of_ramen and customers:
#     ramen = bowls_of_ramen.pop()
#     client = customers.popleft()
#
#     if ramen == client:
#         continue
#
#     if ramen > client:
#         ramen -= client
#         bowls_of_ramen.append(ramen)
#
#     elif ramen < client:
#         client -= ramen
#         customers.appendleft(client)
#
# if len(customers) == 0:
#     print(f"Great job! You served all the customers.")
#     if bowls_of_ramen:
#         print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls_of_ramen)}")
#
# elif len(customers) > 0:
#     print(f"Out of ramen! You didn't manage to serve all customers.")
#     if customers:
#         print(f"Customers left: {', '.join(str(x) for x in customers)}")

if __name__ == '__main__':
    RamenShop()