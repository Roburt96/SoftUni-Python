def add_book_(add_book):
    if add_book not in shelf_with_books:
        shelf_with_books.insert(0, add_book)


def take_book_(take_book):
    if take_book in shelf_with_books:
        shelf_with_books.remove(take_book)


def swap_book_(one, two):
    if one in shelf_with_books and two in shelf_with_books:
        book_one, book_two = shelf_with_books.index(one), shelf_with_books.index(two)
        shelf_with_books[book_one], shelf_with_books[book_two] = shelf_with_books[book_two], shelf_with_books[book_one]


def insert_book_(insert_book):
    shelf_with_books.append(insert_book)


def check_book_(check_book_index):
    if 0 <= check_book_index < len(shelf_with_books):
        print(f"{shelf_with_books[check_book_index]}")


shelf_with_books = input().split('&')

command = input()
while command != 'Done':
    command_type, *data = command.split(" | ")


    if "Add Book" in command_type:
        add_book = data[0]
        add_book_(add_book)

    elif 'Take Book' in command_type:
        take_book = data[0]
        take_book_(take_book)

    elif 'Swap Books' in command_type:
        swap_book_one = data[0]
        swap_book_two = data[1]
        swap_book_(swap_book_one, swap_book_two)

    elif 'Insert Book' in command_type:
        insert_book = data[0]
        insert_book_(insert_book)

    elif 'Check Book' in command_type:
        check_book = int(data[0])
        check_book_(check_book)

    command = input()

print(', '.join(shelf_with_books))