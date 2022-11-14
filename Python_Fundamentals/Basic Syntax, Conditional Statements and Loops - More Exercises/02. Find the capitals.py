word = input()
capitals = []
for i in range(len(word)):
    if word[i].isupper():
        capitals.append(i)
    else:
        continue
print(capitals)
