words = [x for x in input().split()]
new_list_words = []

for len_words in range(len(words)):
    len_word = len(words[len_words])
    new_list_words += words[len_words] * len(words[len_words])

print(''.join(new_list_words))
