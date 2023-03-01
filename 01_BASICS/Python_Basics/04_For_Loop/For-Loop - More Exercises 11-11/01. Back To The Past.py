amount = float(input())
death_year = int(input())
current_age = 18
even_year_spending = 12000.0

for age in range(1800, death_year + 1):

    if age % 2 == 0:
        amount -= even_year_spending
        age += 1
        current_age += 1

    elif age % 2 == 1:
        odd_year_spending = 12000.0 + (50 * current_age)
        amount -= odd_year_spending
        age += 1
        current_age += 1

if amount >= 0:
    print(f"Yes! He will live a carefree life and will have {amount:.2f} dollars left.")
elif amount < 0:
    print(f"He will need {abs(amount):.2f} dollars to survive.")
