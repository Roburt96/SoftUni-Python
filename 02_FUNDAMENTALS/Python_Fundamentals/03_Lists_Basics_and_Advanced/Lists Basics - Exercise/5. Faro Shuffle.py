cards, shuffle = input().split(), int(input())
lenght = len(cards)
mid = int(lenght / 2)


for i in range(shuffle):
    lst = []
    for p in range(0, mid):
        lst.append(cards[p])
        lst.append(cards[mid])
        mid += 1
    cards = lst
    mid = int(lenght / 2)

print(lst)
