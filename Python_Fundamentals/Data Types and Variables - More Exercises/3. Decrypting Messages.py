# key = int(input())
# lines = int(input())
# msg = []
#
# for i in range(lines):
#     ord_letters = chr(ord(input()) + key)
#     msg.append(ord_letters)
#
# print(*msg, sep='')


def secret_message(enter_key, line):
    for i in range(line):
        ord_letters = chr(ord(input()) + enter_key)
        msg.append(ord_letters)



key = int(input())
lines = int(input())
msg = []

secret_message(key, lines)
print(*msg, sep='')

