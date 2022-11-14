word = input()
reversed_word = ''

# -1 length minus one, loop until 0 (-1)
# last -1 step backward
for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]
print(reversed_word)
