msg = int(input())

for i in range(msg + 1):
    num = int(input())
    if num == 88:
        print('Hello')
    elif num == 86:
        print('How are you?')
    elif num != 88 and num != 86 and num < 88:
        print('GREAT!')
    elif num > 88:
        print('Bye.')


