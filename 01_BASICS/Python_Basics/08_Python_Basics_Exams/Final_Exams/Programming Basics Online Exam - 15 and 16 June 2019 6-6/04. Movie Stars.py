budget = float(input())
honorar = 0
actor_name = input()


while actor_name != "ACTION":

    if len(actor_name) <= 15:
        honorar = float(input())
    else:
        honorar = budget * 20/100

    budget -= honorar

    if budget <= 0:
        print(f"We need {abs(budget):.2f} leva for our actors.")
        break
    actor_name = input()

if budget > 0:
    print(f"We are left with {budget:.2f} leva.")
