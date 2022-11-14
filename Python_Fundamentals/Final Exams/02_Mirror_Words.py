import re

text_string = input()
pattern = re.compile(r"(@|#)(?P<word>[a-zA-Z]{3,})(\1{2})(?P<word2>[a-zA-Z]{3,})\1")

result = list(re.finditer(pattern, text_string))

pairs = [x['word'] for x in result]

if len(pairs) == 0:
    print("No word pairs found!")

elif len(pairs) > 0:
    print(f"{len(pairs)} word pairs found!")


final_mirror_words = []
for word_pairs in result:
    if len(word_pairs['word']) == len(word_pairs['word2']):
        if word_pairs['word'] == word_pairs['word2'][::-1]:
            final_mirror_words.append(f"{word_pairs['word']} <=> {word_pairs['word2']}")

if len(final_mirror_words) > 0:
    print("The mirror words are:")
    print(', '.join(final_mirror_words))
else:
    print("No mirror words!")



