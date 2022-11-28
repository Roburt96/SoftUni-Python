n_nums = int(input())
nums = []
for x in range(n_nums):
    number = int(input())
    nums.append(number)

print(f"Sum = {sum(nums)}")
print(f"Min = {min(nums)}")
print(f"Max = {max(nums)}")
print(f"Average = {sum(nums) / len(nums)}")
