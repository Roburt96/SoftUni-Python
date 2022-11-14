number_of_pieces = int(input())
information = {}
for i in range(number_of_pieces):
    piece, composer, key = input().split("|")
    information[piece] = information.get(piece, {'composer': composer, 'key': key})


def add_(piece, composer, key):

    if piece not in information:
            information[piece] = information.get(piece, {'composer': composer, 'key': key})
            print(f"{piece} by {composer} in {key} added to the collection!")

    else:
        print(f"{piece} is already in the collection!")


def remove_(piece):
    try:
        information.pop(piece)
        print(f"Successfully removed {piece}!")
    except:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def changekey_(piece, new_key):
    try:
        information[piece]['key'] = new_key
        print(f"Changed the key of {piece} to {new_key}!")

    except:
        print(f"Invalid operation! {piece} does not exist in the collection.")


command = input()
while command != 'Stop':
    cmd, *info = command.split("|")

    if 'Add' in cmd:
        piece = info[0]
        composer = info[1]
        key = info[2]
        add_(piece, composer, key)

    elif 'Remove' in cmd:
        piece = info[0]
        remove_(piece)

    elif 'ChangeKey' in cmd:
        piece = info[0]
        new_key = info[1]
        changekey_(piece, new_key)
    command = input()


for piece in information.keys():
    print(f"{piece} -> Composer: {information[piece]['composer']}, Key: {information[piece]['key']}")
