# string = input()[::-1]
# print(string)


string = list(input())
stack = []

for i in range(len(string)):
    stack.append(string.pop())

print("".join(stack))
