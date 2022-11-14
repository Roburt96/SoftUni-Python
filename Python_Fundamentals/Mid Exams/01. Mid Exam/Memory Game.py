elements = input().split()
command = input()
turns = 0

def remove_twins(index1, index2):
    global elements
    print(f"Congrats! You have found matching elements - {elements[index1]}!")
    elements = [x for x in elements if x != elements[index1]]



def cheat(index1, index2):
    insert_num = f"-{turns}a"
    middle_pairs = len(elements) // 2
    elements.insert(middle_pairs, insert_num), \
                elements.insert(middle_pairs, insert_num)
    print(f"Invalid input! Adding additional elements to the board")


while command != "end":
    indexes = command.split()
    index1 = int(indexes[0])
    index2 = int(indexes[1])
    turns += 1
    # if (index1 >= 0 and index1 < len(elements)) and (index2 >= 0 and index2 < len(elements)):
    # out_of_bound_checker = [index for index in indexes if 0 > int(index) or int(index) >= len(elements)]
    if ((0 > index1 or index1 >= len(elements)) or (0 > index2 or index2 >= len(elements))) \
        or index1 == index2:

    # if out_of_bound_checker or index1 == index2:
        cheat(index1, index2)

    elif elements[index1] == elements[index2]:
        remove_twins(index1, index2)

    elif elements[index1] != elements[index2]:
        print("Try again!")

    if not elements:
        print(f"You have won in {turns} turns!")
        break

    command = input()

if elements:
    print("Sorry you lose :(")
    print(*elements)

