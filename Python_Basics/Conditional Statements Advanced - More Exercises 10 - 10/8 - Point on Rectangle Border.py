x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

if abs(x) == abs(x1) and y1 <= y <= y2 \
        or abs(x) == abs(x2) and y1 <= y <= y2\
        or abs(y) == abs(y1) and x1 <= x <= x1 \
        or abs(y) == abs(y2) and x1 <= x <= x2:
    print("Border")
else:
    print("Inside / Outside")
