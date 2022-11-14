budget = float(input())
category = input()
people = int(input())

sum_needed = 0
transport = 0
ticket = 0

if category == 'Normal':
    ticket = 249.99
elif category == 'VIP':
    ticket = 499.99

if people >= 1 and people <=4:
    transport = budget - (budget * 0.75)
elif people >= 5 and people <= 9:
    transport = budget - (budget * 0.60)
elif people >= 10 and people <= 24:
    transport = budget - (budget * 0.50)
elif people >= 25 and people <= 49:
    transport = budget - (budget * 0.40)
elif people >= 50:
    transport = budget - (budget * 0.25)

sum_needed = ticket * people
sum_lack = sum_needed - transport
sum_over = transport - sum_needed

if sum_needed > transport:
    print(f'Not enough money! You need {sum_lack:.2f} leva.')
elif sum_needed < transport:
    print(f'Yes! You have {sum_over:.2f} leva left.')
