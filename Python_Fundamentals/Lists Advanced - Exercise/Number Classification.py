numbers = [int(x) for x in input().split(",")]
positive = []
negative = []
even = []
odd = []

for i in numbers:
    if i >= 0:
        positive.append(str(i))
    if i < 0:
        negative.append(str(i))
    if i % 2 == 0:
        even.append(str(i))
    if i % 2 != 0:
        odd.append(str(i))

print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")


# numbers = [int(x) for x in input().split(",")]
#
# print(f"Positive: {', '.join(str(x) for x in numbers if x >= 0)}")
# print(f"Negative: {', '.join(str(x) for x in numbers if x < 0)}")
# print(f"Even: {', '.join(str(x) for x in numbers if x % 2 == 0)}")
# print(f"Odd: {', '.join(str(x) for x in numbers if x % 2 != 0)}")
