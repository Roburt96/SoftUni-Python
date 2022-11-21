import sys

n_lines = int(input())
longest_intersection = -sys.maxsize
set_a = set()
set_b = set()
current_intersection = set()


for i in range(n_lines):
    cords = input().split("-")
    a = [int(i) for i in cords[0].split(",")]
    b = [int(i) for i in cords[1].split(",")]

    for z in range(a[0], a[1] + 1):
        set_a.add(z)
    for x in range(b[0], b[1] + 1):
        set_b.add(x)

    x = set_a.intersection(set_b)
    if len(x) > longest_intersection:
        longest_intersection = len(x)
        current_intersection = x
    set_a = set()
    set_b = set()

print(f"Longest intersection is [", end="")
print(*current_intersection, sep=", ", end="")
print(f"] with length {len(current_intersection)}")
