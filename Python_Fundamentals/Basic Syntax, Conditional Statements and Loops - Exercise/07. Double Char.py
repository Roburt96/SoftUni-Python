text = input()
while text != 'End':
    if text != 'SoftUni':
        for char in text:
            print(char * 2, end='')
        print()
    text = input()
