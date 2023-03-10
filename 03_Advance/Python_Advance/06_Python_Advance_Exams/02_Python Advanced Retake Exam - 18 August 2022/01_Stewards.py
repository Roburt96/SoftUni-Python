from collections import deque

seats = input().split(", ")
row_one_numbers = deque(int(x) for x in input().split(', '))
row_two_numbers = deque(int(x) for x in input().split(', '))
counter, find_seats = 0, []

while len(find_seats) != 3 and counter != 10:

    num_row_one = row_one_numbers.popleft()
    num_row_two = row_two_numbers.pop()
    counter += 1
    letter_seat = chr(num_row_one + num_row_two)

    find = False
    for seat in (f"{num_row_one}{letter_seat}", f"{num_row_two}{letter_seat}"):
        if seat in seats:
            find_seats.append(seat)
            seats.remove(seat)
            find = True

    if find:
        continue

    row_one_numbers.append(num_row_one)
    row_two_numbers.appendleft(num_row_two)

print(f"Seat matches: {', '.join(find_seats)}")
print(f"Rotations count: {counter}")


# class Stewards:
#     counter = 0
#     find_seats = []
#
#     def __init__(self, seats: list, nums_one: deque, nums_two: deque):
#         self.seats = list()
#         self.nums_one = deque()
#         self.nums_two = deque()
#
#     def check_seat(self):
#         global is_find
#
#         row_one = self.nums_one.popleft()
#         row_two = self.nums_two.pop()
#         Stewards.counter += 1
#         letter_seat = chr(row_one + row_two)
#
#         for seat in (f"{row_one}{letter_seat}", f"{row_two}{letter_seat}"):
#             if seat in self.seats:
#                 Stewards.find_seats.append(seat)
#                 self.seats.remove(seat)
#                 is_find = True
#             else:
#                 self.nums_one.append(row_one)
#                 self.nums_two.appendleft(row_two)
#
#
# if __name__ == '__main__':
#     is_find = False
#     seats_list = input().split(", ")
#     row_one_numbers = deque(int(x) for x in input().split(', '))
#     row_two_numbers = deque(int(x) for x in input().split(', '))
#     steward = Stewards(seats_list, row_one_numbers, row_two_numbers)
#     while steward.nums_one and steward.nums_two:
#         steward.check_seat()
#         if is_find:
#             continue
#
#     print(f"Seat matches: {', '.join(steward.find_seats)}")
#     print(f"Rotations count: {steward.counter}")
