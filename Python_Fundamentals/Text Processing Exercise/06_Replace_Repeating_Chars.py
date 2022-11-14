string = input()

letter = ''
new_string = ''

for ch in string:
    if ch != letter:
        letter = ch
        new_string += letter

print(new_string)
