n = int(input())
positive = []
negative = []
count_positive = 0
sum_negative = 0

for i in range(n):
    numbers = int(input())
    if numbers >= 0:
        positive.append(numbers)
        count_positive += 1
    elif numbers < 0:
        negative.append(numbers)
        sum_negative += numbers

print(positive)
print(negative)
print(f'Count of positives: {count_positive}')
print(f'Sum of negatives: {sum_negative}')