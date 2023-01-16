def sum(num):
    even = 0
    odd = 0
    for i in num:
        i = int(i)
        if i % 2 == 0:
            even += i
        else:
            odd += i
    return f"Odd sum = {odd}, Even sum = {even}"


number = input()
print(sum(number))
