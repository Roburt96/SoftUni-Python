class Book:

    def __init__(self, name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages

    def get_book(self):
        return self.name

    def get_author(self):
        return self.author

    def get_pages(self):
        return self.pages





book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)