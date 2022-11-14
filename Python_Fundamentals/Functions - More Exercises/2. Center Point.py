from math import floor


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


def cartesian(X1, X2, Y1, Y2):
    X1 = abs(X1)
    Y1 = abs(Y1)
    X2 = abs(X2)
    Y2 = abs(Y2)
    sum1 = (X1 + Y1)
    sum2 = (X2 + Y2)


    if sum1 > sum2:
        print(f"({floor(x2)}, {floor(y2)})")
    elif sum1 == sum2 or sum2 > sum1:
        print(f"({floor(x1)}, {floor(y1)})")


cartesian(x1, x2, y1, y2)
