deposit = int(input())
term_of_the_deposit = int(input())
annual_interest_rate = float(input())

interest = float(deposit * annual_interest_rate / 100)

interest_one_month = float(interest / 12)

total_money = (f"{deposit + term_of_the_deposit * interest_one_month}")
print(total_money)