
nums = [int(x) for x in input().split()]
num = sorted(nums, reverse=True)
num = num[:3]
print(*num)
