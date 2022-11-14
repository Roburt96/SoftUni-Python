most_powerful_word_counter = 0
most_powerful_word = ''

while True:
    word = input()

    if word == "End of words":
        break

    current_counter_of_chars = 0

    for ch in word:
        current_counter_of_chars += ord(ch)
    print(current_counter_of_chars)