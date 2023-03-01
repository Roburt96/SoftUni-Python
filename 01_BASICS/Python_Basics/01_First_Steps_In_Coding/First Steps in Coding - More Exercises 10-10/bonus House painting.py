x = float(input())
y = float(input())
h = float(input())

side_wall = x * y
window = 1.5 * 1.5
two_sides = 2 * side_wall - 2 * window
back_side = x * x
door = 1.2 * 2
front_and_back = 2 * back_side - door
total_sides = two_sides + front_and_back
green_dye = total_sides / 3.4
print(f"{green_dye: .2f}")

two_roof = 2 * (x * y)
two_triangle = 2 * ((x * h) / 2)

total_roof = two_roof + two_triangle
red_dye = total_roof / 4.3
print(f"{red_dye: .2f}")