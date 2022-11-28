numbers = [x for x in input().split()]
nums = {}
for i in numbers:
    if i not in nums:
        nums[i] = 1
    else:
        nums[i] += 1


for key, value in sorted(nums.items()):
    print(f"{key} -> {value}")
