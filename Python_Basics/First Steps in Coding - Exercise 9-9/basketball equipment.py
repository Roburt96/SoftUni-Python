price_for_one_year = int(input())

price_for_shoes = price_for_one_year - price_for_one_year * 0.40
price_for_basketball_cloth = price_for_shoes - price_for_shoes * 0.20
price_for_basketball_ball = price_for_basketball_cloth / 4
price_for_basketball_accesoary = price_for_basketball_ball / 5


total_sum = price_for_one_year + price_for_shoes + price_for_basketball_cloth + \
            price_for_basketball_accesoary + price_for_basketball_ball
print(total_sum)