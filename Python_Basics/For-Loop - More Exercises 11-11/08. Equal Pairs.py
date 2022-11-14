n = int(input())

first_equal = int(input()) + int(input())
maxdiff = 0

for i in range(n - 1):
    second_equal = int(input()) + int(input())

    if (abs(first_equal - second_equal)) > maxdiff:
        maxdiff = abs(first_equal - second_equal)

    first_equal = second_equal

if maxdiff == 0:
    print(f"Yes, value={first_equal}")
else:
    print(f"No, maxdiff={maxdiff}")
