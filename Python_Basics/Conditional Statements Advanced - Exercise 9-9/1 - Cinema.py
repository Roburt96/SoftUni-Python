screening_type = input()
rown = int(input())
columns = int(input())
income = 0

cinema_capacity = rown * columns
if screening_type == "Premiere":
    income = cinema_capacity * 12
elif screening_type == "Normal":
    income = cinema_capacity * 7.50
elif screening_type == "Discount":
    income = cinema_capacity * 5.00

print(f"{income:.2f} leva")
