number_of_names = int(input())
names = set()
for i in range(number_of_names):
    name = input()
    names.add(name)

print('\n'.join(names))
