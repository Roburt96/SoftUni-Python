one_year_tax = int(input())
shoes = one_year_tax - (one_year_tax * 0.40)
team_clothes = shoes - (shoes * 0.20)
ball = (team_clothes * 1) / 4
accessory = (ball * 1) / 5
total_price = one_year_tax + shoes + team_clothes + ball + accessory
print(f"{total_price:.2f}")
