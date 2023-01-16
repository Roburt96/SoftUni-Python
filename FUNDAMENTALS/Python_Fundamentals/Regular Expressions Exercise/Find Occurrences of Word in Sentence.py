import re

text = input().lower()
word = input()

pattern = re.compile(rf"{word}\b")

result = re.finditer(pattern, text)

len_result = [x for x in result]
print(len(len_result))
