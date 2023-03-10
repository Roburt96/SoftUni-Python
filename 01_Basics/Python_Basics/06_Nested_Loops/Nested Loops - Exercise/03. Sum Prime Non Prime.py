
prime_sum = 0
non_prime_sum = 0

while True:
    num = input()
    non_prime = False
    if num == "stop":
        break
    num = int(num)
    if num < 0:
        print("Number is negative.")
        continue
    elif num == 1:
        non_prime = True
    else:
        for i in range(2, num):
            if num % i == 0 and num != 2:
                non_prime = True
                break
    if non_prime:
        non_prime_sum += num
    else:
        prime_sum += num

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")
