num = int(input())
for first_digit in range(1, 10):
    for second_digit in range(1, 10):
        for third_digit in range(1, 10):
            for fourth_digit in range(1, 10):
                if first_digit + second_digit == third_digit + fourth_digit:
                    if num % (first_digit + second_digit) == 0:
                        print(f"{first_digit}{second_digit}{third_digit}{fourth_digit}", end=" ")
