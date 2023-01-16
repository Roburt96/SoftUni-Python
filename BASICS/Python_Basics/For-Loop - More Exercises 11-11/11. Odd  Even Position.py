from sys import maxsize

n = int(input())
oddSum = 0
oddMin = maxsize
oddMax = -maxsize
evenSum = 0
evenMin = maxsize
evenMax = -maxsize

for i in range(0, n):
    element = float(input())
    if i % 2 == 1:
        evenSum += element
        if element < evenMin:
            evenMin = element
        if element > evenMax:
            evenMax = element
    else:
        oddSum += element
        if element < oddMin:
            oddMin = element
        if element > oddMax:
            oddMax = element
if n > 0:
    print(f"OddSum={oddSum:.2f},")

    if oddMin == maxsize:
        print(f"OddMin=No,")
    else:
        print(f"OddMin={oddMin:.2f},")
    if oddMax == -maxsize:
        print(f"PddMax=No,")
    else:
        print(f"OddMax={oddMax:.2f},")

    print(f"EvenSum={evenSum:.2f},")

    if evenMin == maxsize:
        print(f'EvenMin=No,')
    else:
        print(f'EvenMin={evenMin:.2f},')

    if evenMax == -maxsize:
        print(f'EvenMax=No')
    else:
        print(f'EvenMax={evenMax:.2f}')
elif n == 0:
    print(f"""OddSum=0.00,
    OddMin=No,
    OddMax=No,
    EvenSum=0.00,
    EvenMin=No,
    EvenMax=No""")
else:
    print(f'OddSum={oddSum},')
    print(f'OddMin={oddMin},')
    print(f'OddMax={oddMax},')
    print(f'EvenSum={evenSum:},')
    print(f'EvenMin={evenMin:},')
    print(f'EvenMax={evenMax}')
