word1, word2 = input().split()

total_sum = 0

if len(word1) < len(word2):
    for index in range(len(word1)):
        total_sum += ord(word1[index]) * ord(word2[index])
    for index in range(len(word1), len(word2)):
        total_sum += ord(word2[index])
elif len(word1) > len(word2):
    for index in range(len(word2)):
        total_sum += ord(word1[index]) * ord(word2[index])
    for index in range(len(word2), len(word1)):
        total_sum += ord(word1[index])
else:
    for index in range(len(word1)):
        total_sum += ord(word1[index]) * ord(word2[index])


print(total_sum)