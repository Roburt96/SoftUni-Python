
def get_primes(nums):
    max_num = max(nums)
    primes = []
    for num in range(2, max_num):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    for n in nums:
        if n in primes:
            yield n

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))