number_of_electrons = int(input())
list_electrons = []
x = 0

while 0 <  number_of_electrons:
    x += 1
    electrons = 2 * x ** 2

    if number_of_electrons >= electrons:
        list_electrons.append(electrons)
        number_of_electrons -= electrons
    else:
        list_electrons.append(number_of_electrons)
        number_of_electrons = 0

print(list_electrons)

