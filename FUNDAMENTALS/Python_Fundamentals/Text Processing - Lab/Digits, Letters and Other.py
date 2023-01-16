text = input()
all_digits = ''
all_letters = ''
all_symbols = ''

for ch in range(len(text)):
    if text[ch].isdigit():
        all_digits += text[ch]
    elif text[ch].isalpha():
        all_letters += text[ch]
    else:
        all_symbols += text[ch]

print(all_digits)
print(all_letters)
print(all_symbols)