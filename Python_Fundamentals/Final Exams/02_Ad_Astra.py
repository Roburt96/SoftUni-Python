import re

text = input()
pattern = re.compile(r"([#|\|])(?P<item>[A-Za-z ]+)\1(?P<date>[\d]{2}\/[\d]{2}\/[\d]{2})\1(?P<cal>[\d]+)\1")
result = re.finditer(pattern, text)

cal = 0
food_per_day = 2000
products = list()
for item in result:
    cal += int(item['cal'])
    products.append(f"Item: {item['item']}, Best before: {item['date']}, Nutrition: {item['cal']}")
days = cal // food_per_day
print(f"You have food to last you for: {days} days!")

for prints in products:
    print(prints)
