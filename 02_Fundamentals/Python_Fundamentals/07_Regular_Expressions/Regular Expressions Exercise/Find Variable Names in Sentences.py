import re

text = input()
words = []

pattern = re.compile(r"\b\_(?P<word>[A-Za-z\d]+)\b")
result = re.finditer(pattern, text)

for match in result:
    name = match['word']
    words.append(name)

print(*words, sep=',')