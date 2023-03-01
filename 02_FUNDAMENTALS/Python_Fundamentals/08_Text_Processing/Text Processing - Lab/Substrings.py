remove_word = input()
word = input()
# word = input().replace(remove_word, '')

while remove_word in word:
    word = word.replace(remove_word, '')
print(word)

