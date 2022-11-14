list_one = input().split(", ")
list_two = input().split(", ")
new_list = []
for item in list_one:
    for item2 in list_two:
        if item in item2:
            new_list.append(item)
            break

print(new_list)










