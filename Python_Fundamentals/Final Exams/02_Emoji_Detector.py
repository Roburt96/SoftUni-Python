import re

text = input()

pattern = re.compile(r'(?P<all_sum_word>(::|\*\*)(?P<clear_word>[A-Z][a-z]{2,})(\2))')
digits_pattern = re.compile(r'[0-9]+')

result_text = list(re.finditer(pattern, text))
result_digits = re.finditer(digits_pattern, text)

list_digits = [x for x in text if x.isdigit()]
result_multi_digits = 1
for multiply in list_digits:
    result_multi_digits *= int(multiply)
print(f"Cool threshold: {result_multi_digits}")
print(f"{len(result_text)} emojis found in the text. The cool ones are:")

for res_animal in result_text:
    ch_sum = 0
    for ch in res_animal['clear_word']:
        ord_ch = ord(ch)
        ch_sum += ord_ch
    if ch_sum > result_multi_digits:
        print(f"{res_animal['all_sum_word']}")



