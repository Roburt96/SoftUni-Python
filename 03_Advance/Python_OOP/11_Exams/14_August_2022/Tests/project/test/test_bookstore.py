from project.bookstore import Bookstore
from unittest import TestCase

class TestBookstore(TestCase):

    def setUp(self) -> None:
        self.bookstore = Bookstore(10)

    def test_successfully_init(self):
        self.assertEqual(self.bookstore.books_limit, 10)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {})
        self.assertEqual(self.bookstore.total_sold_books, 0)

    def test_raise_error_for_book_limit(self):
        with self.assertRaises(ValueError) as ve:
            self.newbookstore = Bookstore(0)
        self.assertEqual(str(ve.exception), "Books limit of 0 is not valid")

    def test_no_space_for_more_books(self):
        with self.assertRaises(Exception) as error:
            self.bookstore.receive_book("Book 1", 11)
        self.assertEqual(str(error.exception), "Books limit is reached. Cannot receive more books!")

    def test_successfully_receive_book(self):
        result = self.bookstore.receive_book("receive", 5)
        self.assertEqual(result, "5 copies of receive are available in the bookstore.")

        result_2 = self.bookstore.receive_book("receive", 5)
        self.assertEqual(result_2, "10 copies of receive are available in the bookstore.")

        self.assertEqual(10, len(self.bookstore))


    def test_book_not_available(self):
        self.bookstore.availability_in_store_by_book_titles = {}
        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book("Book 2", 1)
        self.assertEqual(str(error.exception), "Book Book 2 doesn't exist!")

    def test_no_more_copies_of_book(self):
        self.bookstore.availability_in_store_by_book_titles = {"Book 2": 5}
        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book("Book 2", 6)
        self.assertEqual(str(error.exception), "Book 2 has not enough copies to sell. Left: 5")

    def test_successfully_sell_book(self):
        self.bookstore.availability_in_store_by_book_titles = {"selling": 10}
        result = self.bookstore.sell_book("selling", 2)
        self.assertEqual(result, "Sold 2 copies of selling")
        self.assertEqual(len(self.bookstore), 8)
        self.assertEqual(self.bookstore.total_sold_books, 2)

        result_2 = self.bookstore.sell_book("selling", 8)
        self.assertEqual(result_2, "Sold 8 copies of selling")
        self.assertEqual(len(self.bookstore), 0)
        self.assertEqual(self.bookstore.total_sold_books, 10)

        self.assertEqual(str(self.bookstore), "Total sold books: 10\n"
                                              "Current availability: 0\n"
                                              " - selling: 0 copies")



