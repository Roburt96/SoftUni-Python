import re

text = input()
pattern = (r"[@|#]+(?P<key>[a-z]{3,})[@|#]+[\W]*(?P<num>[0-9]+)[\/]+")
result = re.finditer(pattern, text)

for item in result:
    print(f"You found {item['num']} {item['key']} eggs!")
