import sys

command = ''
movies = 0
best_movie = ''
max_ASCII = -sys.maxsize

while command != 'STOP' and movies < 7:
    command = input()
    ASCII = 0
    total_ASCII = 0
    if command == "STOP":
        print(f"The best movie for you is {best_movie} with {max_ASCII} ASCII sum.")
        break

    movies += 1
    for i in range(len(command)):
        ascii_converting = ord(command[i])
        if (command[i]) >= "A" and command[i] <= "Z":
            ASCII = ascii_converting - len(command)
        elif (command[i]) >= "a" and command[i] <= "z":
            ASCII = ascii_converting - len(command) * 2
        else:
            ASCII = ascii_converting
        total_ASCII += ASCII
        if total_ASCII > max_ASCII:
            max_ASCII = total_ASCII
            best_movie = command
        if movies == 7:
            print(f"The limit is reached.")
            print(f"The best movie for you is {best_movie} with {max_ASCII} ASCII sum.")
            break
