book_name = input()

next_book = input()

book_found = False
counter = 0

while next_book != "No More Books":
    if next_book == book_name:
        book_found = True
        break

    next_book = input()
    counter += 1

if not book_found:
    print("The book you search is not here!")
    print(f"You checked {counter} books.")
else:
    print(f"You checked {counter} books and found it.")
