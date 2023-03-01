from collections import deque
#
# queue = deque()
# while True:
#     cmd = input()
#     if cmd == "Paid":
#         while len(queue):
#             print(queue.popleft())
#     elif cmd == "End":
#         print(f"{len(queue)} people remaining.")
#         break
#     else:
#         queue.append(cmd)

from collections import deque
class Supermarket:

    def __init__(self):
        self.string = deque()
        self.main_func()

    def main_func(self):
        while True:
            command = input()
            if command == 'End':
                print(f"{len(self.string)} people remaining.")
                break
            elif command == 'Paid':
                while len(self.string):
                    print(self.string.popleft())
            else:
                self.string.append(command)

market = Supermarket()
