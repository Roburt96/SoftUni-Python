number_of_rooms = int(input())
room_number = 0
free_chairs = 0
total_visitors = 0


for room in range(1, number_of_rooms + 1):
    room_number += 1
    chairs_visitors = input().split()
    chairs = [x for x in chairs_visitors[0]]
    visitors = int(chairs_visitors[1])
    total_visitors += visitors
    free_chairs += len(chairs)
    if len(chairs) < visitors:
        print(f"{abs(len(chairs) - visitors)} more chairs needed in room {room_number}")
if total_visitors <= free_chairs:
    print(f"Game On, {free_chairs - total_visitors} free chairs left")

