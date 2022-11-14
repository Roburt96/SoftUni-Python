geometric = str(input())

import math
from math import pi


square = "square"
rectangle = "rectangle"
circle = "circle"
triangle = "triangle"

if geometric == square:
    square_side_1 = float(input())
    square_face = square_side_1 * square_side_1
    print(f"{square_face: .3f}")

elif geometric == rectangle:
    rectangle_side_1 = float(input())
    rectangle_side_2 = float(input())
    rectangle_face = rectangle_side_1 * rectangle_side_2
    print(f"{rectangle_face: .3f}")

elif geometric == circle:
    radius = float(input())
    radius_circle = float(radius * radius * pi)
    print(f"{radius_circle: .3f}")

elif geometric == triangle:
    triangle_side_1 = float(input())
    triangle_side_2 = float(input())
    triangle_face = float((triangle_side_1 * triangle_side_2) / 2)
    print(f"{triangle_face: .3f}")


