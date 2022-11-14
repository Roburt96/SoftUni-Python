numbers = [n for n in input().split()]
message = input()

message_show = " "

for num in numbers:
    find_index = 0
    for sum_num in num:
        find_index += int(sum_num)
    if find_index > len(message):
        find_index = find_index - len(message)
    message_show += message[find_index]
    message = message[:find_index] + message[find_index + 1:]

print(message_show)



