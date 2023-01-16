numbers = list(map(float, input().split()))

res = (abs(ele) for ele in numbers)
print(res)