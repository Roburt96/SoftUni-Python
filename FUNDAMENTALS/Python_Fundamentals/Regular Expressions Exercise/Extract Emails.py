import re

text = input()

pattern = re.compile(r"\b([a-z0-9]+[-_.a-z0-9])*@[a-z]+.([-.a-z]+\b)")

result = re.finditer(pattern, text)

for i in result:
    print(i[0])
