string = input()
emoji = []

for ch in range(len(string)):
    if string[ch] == ':':
        emoji.append(string[ch] + string[ch + 1])

print('\n'.join(emoji))
