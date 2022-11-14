a1 = int(input())
a2 = int(input())
n = int(input())

for char in range(a1, a2):
    symbol = chr(char)

    for s2 in range(1, n):
        symbol2 = s2

        for s3 in range(1, n // 2 ):
            symbol3 = s3

            if char % 2 != 0 and (symbol2 + symbol3 + char) % 2 != 0:
                print(f"{symbol}-{symbol2}{symbol3}{char}")
