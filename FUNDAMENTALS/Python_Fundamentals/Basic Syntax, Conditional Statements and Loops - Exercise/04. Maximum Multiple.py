divisor = int(input())
boundary = int(input())
max_multi = 0
for curr_num in range(boundary, divisor, -1):
    if curr_num % divisor == 0:
        max_multi = curr_num
        break
print(max_multi)


