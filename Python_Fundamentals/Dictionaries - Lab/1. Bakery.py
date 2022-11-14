element = input().split(" ")
bakery = {}

for i in range(0, len(element), 2):
    key = element[i]
    value = element[i + 1]
    bakery[key] = int(value)
print(bakery)
