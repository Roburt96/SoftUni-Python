# number_of_pieces = int(input())
# information = {}
# for i in range(number_of_pieces):
#     piece, composer, key = input().split("|")
#     information[piece] = information.get(piece, {'composer': composer, 'key': key})
#
#
# def add_(piece, composer, key):
#
#     if piece not in information:
#             information[piece] = information.get(piece, {'composer': composer, 'key': key})
#             print(f"{piece} by {composer} in {key} added to the collection!")
#
#     else:
#         print(f"{piece} is already in the collection!")
#
#
# def remove_(piece):
#     try:
#         information.pop(piece)
#         print(f"Successfully removed {piece}!")
#     except:
#         print(f"Invalid operation! {piece} does not exist in the collection.")
#
#
# def changekey_(piece, new_key):
#     try:
#         information[piece]['key'] = new_key
#         print(f"Changed the key of {piece} to {new_key}!")
#
#     except:
#         print(f"Invalid operation! {piece} does not exist in the collection.")
#
#
# command = input()
# while command != 'Stop':
#     cmd, *info = command.split("|")
#
#     if 'Add' in cmd:
#         piece = info[0]
#         composer = info[1]
#         key = info[2]
#         add_(piece, composer, key)
#
#     elif 'Remove' in cmd:
#         piece = info[0]
#         remove_(piece)
#
#     elif 'ChangeKey' in cmd:
#         piece = info[0]
#         new_key = info[1]
#         changekey_(piece, new_key)
#     command = input()
#
#
# for piece in information.keys():
#     print(f"{piece} -> Composer: {information[piece]['composer']}, Key: {information[piece]['key']}")


# pieces_information = {}

class Pianist:

    def __init__(self):
        self.piece = {}

    def delete_(self, piece_name):
        del self.piece[piece_name]
        print(f"Successfully removed {piece_name}!")

    def changekey_(self, new_key, piece_name):
        current_key = self.piece[piece_name]['key']
        self.piece[piece_name]['key'] = new_key
        print(f"Changed the key of {current_key} to {self.piece[piece_name]['key']}!")

    def __repr__(self):
        print(f"{self.piece} -> Composer: {self.piece['composer']}, Key: {self.piece['key']}")

number_of_pieces = int(input())

all_pieces = Pianist()
for i in range(number_of_pieces):
    piece, composer, key = input().split("|")
    all_pieces.piece[piece] = all_pieces.piece.get(piece, {'composer': composer, 'key': key})

commands = input()
while commands != 'Stop':
    cmd_type, *info = commands.split("|")
    if 'Add' in cmd_type:
        piece_name = info[0]
        composer = info[1]
        key = info[2]
        if piece_name in all_pieces.piece:
            print(f"{piece_name} is already in the collection!")
        else:
            all_pieces.piece[piece_name] = all_pieces.piece.get(piece_name, {'composer': composer, 'key': key})

    elif 'Remove' in cmd_type:
        piece_name = info[0]
        if piece_name in all_pieces.piece:
            all_pieces.delete_(piece_name)
        else:
            print(f"Invalid operation! {piece_name} does not exist in the collection.")

    elif 'ChangeKey' in cmd_type:
        piece_name = info[0]
        new_key = info[1]
        if piece_name in all_pieces.piece:
            all_pieces.changekey_(new_key, piece_name)
        else:
            print(f"Invalid operation! {piece_name} does not exist in the collection.")
    commands = input()



for key, value in all_pieces.piece.items():
    print(f"{key} -> Composer: {value['composer']}, Key: {value['key']}")
