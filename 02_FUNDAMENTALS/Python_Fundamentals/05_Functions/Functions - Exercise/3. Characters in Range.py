char_one = input()
char_two = input()


def symbols(start, end):
    start = int(ord(start) + 1)
    end = int(ord(end))
    for n in range(start, end):
        print(chr(n), end=" ")


symbols(char_one, char_two)





