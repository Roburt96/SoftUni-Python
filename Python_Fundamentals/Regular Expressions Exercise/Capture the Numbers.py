import re

pattern = r"\d+"
numbers = []
text = input()

while text:
    if text is None:
        break

    matches = re.findall(pattern, text)
    mat = [match for match in matches]
    [numbers.append(number) for number in mat]
    text = input()

print(*numbers)


