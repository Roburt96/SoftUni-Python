word = input()
vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']
result = ''
for letter in word:
    if letter not in vowels:
        result += letter
print(result)

