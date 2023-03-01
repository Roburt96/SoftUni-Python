n, m = [int(x) for x in input().split()]
set_length_n = set()
set_length_m = set()

for i in range(n):
    numbers_n = int(input())
    set_length_n.add(numbers_n)
for z in range(m):
    numbers_m = int(input())
    set_length_m.add(numbers_m)

set_length_n.intersection_update(set_length_m)
print(*set_length_n, sep="\n")
