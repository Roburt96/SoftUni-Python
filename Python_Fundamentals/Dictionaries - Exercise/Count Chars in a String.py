word = [x for x in input().replace(" ", "")]

char_dict = {}
for char in word:
    if char not in char_dict:
        char_dict[char] = 0
    char_dict[char] += 1

for key, value in char_dict.items():
    print(f"{key} -> {value}")
