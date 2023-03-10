import re

string = input()
# locations = []
pattern = re.compile(r"(=|\/)(?P<destination>[A-Z][A-Za-z]{2,})\1")

result = re.finditer(pattern, string)


location = [x['destination'] for x in result]
points = sum([len(x) for x in location])

print(f"Destinations: {', '.join(location)}")
print(f"Travel Points: {points}")