tail = input()
body = input()
head = input()

list = [tail, body, head]

list[0], list[2] = list[2], list[0]
print(list)



