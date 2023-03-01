characters = input().split(", ")
ascii_dictionaries = {}

# ascii_simvols = ord(characters[2])

for index, symbols in enumerate(characters):
    if characters[index] not in ascii_dictionaries:
        ascii_dictionaries[symbols] = ord(symbols)

print(ascii_dictionaries)

