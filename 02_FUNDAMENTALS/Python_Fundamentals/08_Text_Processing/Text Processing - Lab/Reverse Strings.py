word = input()

while word != "end":
    reverse_word = ''
    for ch in reversed(word):
        reverse_word += ch
    print(f"{word} -> {reverse_word}")

    word = input()

# word = [x for x in input()]
# while word != 'end':
#     reversed_word = ''
#     if word == 'end':
#         break
#     for ch in reversed(word):
#         reversed_word += ch
#     print(f"{''.join(word)} -> {reversed_word}")
#     word.pop()
#
#     word = [x for x in input()]
