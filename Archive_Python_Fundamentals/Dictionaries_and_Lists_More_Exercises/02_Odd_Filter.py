int_numbers = [int(x) for x in input().split()]
odd_num_remove = [int(x) for x in int_numbers if x % 2 != 0]
odd_num = odd_num_remove

for num in odd_num_remove:
    if odd_num_remove[num] > (sum(odd_num) / len(odd_num)):
        odd_num_remove[num] += 1
    else:
        odd_num_remove[num] -= 1

print(odd_num_remove)

