from collections import deque
vowels = deque(input().split())
consonants = deque(input().split())
flowers = {
    "rose": "rose",
    "tulip": "tulip",
    "lotus": "lotus",
    "daffodil": "daffodil"
}

find = False
word = ""

while vowels and consonants and not find:
    first_ch = vowels.popleft()
    second_ch = consonants.pop()
    for key, value in flowers.items():
        if first_ch in value:
            flowers[key] = flowers[key].replace(first_ch, "")
        if second_ch in value:
            flowers[key] = flowers[key].replace(second_ch, "")
        if not flowers[key]:
            word = key
            find = True
            break

if find:
    print(f"Word found: {word}")
elif not find:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
