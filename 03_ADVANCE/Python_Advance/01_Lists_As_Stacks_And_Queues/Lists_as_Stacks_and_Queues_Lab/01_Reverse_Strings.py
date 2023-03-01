# string = input()[::-1]
# print(string)

# print("".join([x for x in input()[::-1]]))

# string = list(input())
# stack = []
#
# for i in range(len(string)):
#     stack.append(string.pop())
#
# print("".join(stack))

class ReverseString:

    def __init__(self, string):
        self.string = list(string)
        self.stack = []

    def main(self):
        for i in range(len(self.string)):
            self.stack.append(self.string.pop())


    def __repr__(self):
        return ''.join(self.stack)

reverse = ReverseString(input())
reverse.main()
print(reverse)
