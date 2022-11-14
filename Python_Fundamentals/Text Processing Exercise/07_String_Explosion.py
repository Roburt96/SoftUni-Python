string = input()
new_string = []
for sym in range(len(string)):
    new_string.append(string[sym])

for ch in range(len(new_string)):
    if string[ch].isdigit():
        new_string.remove(new_string[ch])

print(new_string)
