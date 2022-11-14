car_time = list(map(int, input().split(" ")))
mid_lenght = int(len(car_time)) / 2

left_car = car_time[:int(mid_lenght)]
right_car = reversed(car_time[int(-mid_lenght):])
time_left_car = 0
time_right_car = 0
for f_car in left_car:
    time_left_car += f_car
    if f_car == 0:
        time_left_car *= 0.8
for s_car in right_car:
    time_right_car += s_car
    if s_car == 0:
        time_right_car *= 0.8

if time_left_car < time_right_car:
    print(f"The winner is left with total time: {time_left_car:.1f}")
else:
    print(f"The winner is right with total time: {time_right_car:.1f}")






