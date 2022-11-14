# text = input().split()
# even_words = [x for x in text if len(x) % 2 == 0]
# print(even_words, end="")


# text = [x for x in input().split() if len(x) % 2 == 0]
# print(*text, sep="\n")


[print(x) for x in input().split() if len(x) % 2 == 0]