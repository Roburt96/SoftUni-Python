secret_msg = input().split()
final_msg = []

for signle_word in secret_msg:
    nums = ''
    word = ''
    current_words = []
    for symbol in signle_word:
        if symbol.isdigit():
            nums += symbol
        else:
            current_words.append(symbol)
            pass

    chr_alpha = chr(int(nums))
    current_words.insert(0, chr_alpha)
    if len(current_words) > 2:
        current_words[1], current_words[-1] = current_words[-1], current_words[1]

    for i in current_words:
        word += i
    final_msg.append(word)

print(*final_msg)
