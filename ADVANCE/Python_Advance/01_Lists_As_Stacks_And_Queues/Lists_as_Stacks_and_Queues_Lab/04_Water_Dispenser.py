# from collections import deque
# quantity_of_water = int(input())
# queue = deque()
# name = input()
# while name != 'Start':
#     queue.append(name)
#     name = input()
#
# command = input()
# while command != 'End':
#     if 'refill' in command:
#         litter_to_add = command.split(" ")
#         litters = int(litter_to_add[1])
#         quantity_of_water += litters
#
#     else:
#         liters = int(command)
#         if liters <= quantity_of_water:
#             quantity_of_water -= liters
#             print(f"{queue.popleft()} got water")
#         else:
#             print(f"{queue.popleft()} must wait")
#     command = input()
#
# print(f"{quantity_of_water} liters left")

from collections import deque
class WaterDispenser:

    def __init__(self):
        self.quantity_of_water = int(input())
        self.queue = deque()
        self.msg = []
    def append_in_queue(self):
        name = input()
        while name != 'Start':
            self.queue.append(name)
            name = input()

    def message(self):
        print('\n'.join(self.msg))

    def drink(self):
        self.append_in_queue()
        while True:
            command = input()
            if 'End' in command:
                self.msg.append(f'{self.quantity_of_water} liters left')
                break

            if 'refill' in command:
                liters = int(command.split()[1])
                self.quantity_of_water += liters
            else:
                drink = int(command)
                cur_name = self.queue.popleft()
                if drink <= self.quantity_of_water:
                    self.quantity_of_water -= drink
                    self.msg.append(f'{cur_name} got water')
                else:
                    self.msg.append(f'{cur_name} must wait')

        self.message()

if __name__ == '__main__':
    WaterDispenser().drink()
