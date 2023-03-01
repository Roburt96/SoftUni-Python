number_of_synonyms = int(input())
synonyms_dict = {}

for i in range(number_of_synonyms):
    key = input()
    value = input()

    if key not in synonyms_dict:
        synonyms_dict[key] = []
    synonyms_dict[key].append(value)

for word in synonyms_dict:
    print(f"{word} - {', '.join(synonyms_dict[word])}")
