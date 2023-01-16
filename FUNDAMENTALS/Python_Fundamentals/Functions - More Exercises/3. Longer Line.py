coordinates_point_one = [float(input()) for _ in range(4)]
coordinates_point_two = [float(input()) for _ in range(4)]

abs_coordinates_one = [abs(x) for x in coordinates_point_one]
abs_coordinates_two = [abs(x) for x in coordinates_point_two]

if sum(abs_coordinates_one) > sum(abs_coordinates_two):
    coordinates_point_one = list(map(int, coordinates_point_one))
    if abs_coordinates_one[0] + abs_coordinates_two[1] > abs_coordinates_one[2] + abs_coordinates_two[3]:
        print(f"{coordinates_point_one[2], coordinates_point_one[3]}"
              f"{coordinates_point_one[0], coordinates_point_one[1]}")
    else:
        print(f"{coordinates_point_one[0], coordinates_point_one[1]}"
              f"{coordinates_point_one[2], coordinates_point_one[3]}")


elif sum(abs_coordinates_one) > sum(abs_coordinates_two):
    coordinates_point_two = list(map(int, coordinates_point_two))
    if abs_coordinates_two[0] + abs_coordinates_two[1] > abs_coordinates_two[2] + abs_coordinates_two[3]:
        print(f"{coordinates_point_two[2], coordinates_point_two[3]}"
              f"{coordinates_point_two[0], coordinates_point_two[1]}")
    else:
        print(f"{coordinates_point_two[0], coordinates_point_two[1]}"
              f"{coordinates_point_two[2], coordinates_point_two[3]}")
else:
    coordinates_point_two = list(map(int, coordinates_point_two))
    if abs_coordinates_two[0] + abs_coordinates_two[1] > abs_coordinates_two[2] + abs_coordinates_two[3]:
        print(f"{coordinates_point_two[2], coordinates_point_two[3]}"
              f"{coordinates_point_two[0], coordinates_point_two[1]}")
    else:
        print(f"{coordinates_point_two[0], coordinates_point_two[1]}"
              f"{coordinates_point_two[2], coordinates_point_two[3]}")
