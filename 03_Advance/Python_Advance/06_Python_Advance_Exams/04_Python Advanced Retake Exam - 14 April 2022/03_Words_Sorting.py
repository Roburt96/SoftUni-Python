def words_sorting(*args):
    words = {}
    for word in args:
        sum = 0
        for ch in word:
            sum += ord(ch)
        words[word] = sum
    result = ''
    is_odd = False
    for key, value in words.items():
        if value % 2 != 0:
            is_odd = True
        else:
            is_odd = False

    if is_odd:
        for key, value in sorted(words.items(), key=lambda x: -x[1]):
            result += f"{key} - {value}\n"
        return result
    else:
        for key, value in sorted(words.items(), key=lambda x: x[0]):
            result += f"{key} - {value}\n"
        return result


print(
    words_sorting(
        'cacophony',
        'accolade'
  ))

# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'eye'
#   ))


# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'mythology'
#   ))