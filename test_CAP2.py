import unittest

from CSF101_CAP2_02230292 import Book, Library, Admin, User 

class TestLibraryManagementSystem(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.library.add_book("The Great Gatsby")
        self.library.add_book("1984")

    def test_borrow_book_valid(self):
        result = self.library.borrow_book("The Great Gatsby")
        self.assertTrue(result)
        self.assertFalse(self.library.is_book_available("The Great Gatsby"))

    def test_borrow_book_invalid(self):
        self.library.borrow_book("The Great Gatsby")
        result = self.library.borrow_book("The Great Gatsby")
        self.assertFalse(result)

    def test_return_book_valid(self):
        self.library.borrow_book("1984")
        result = self.library.return_book("1984")
        self.assertTrue(result)
        self.assertTrue(self.library.is_book_available("1984"))

    def test_return_book_invalid(self):
        result = self.library.return_book("The Great Gatsby")
        self.assertFalse(result)

    def test_admin_adding_books(self):
        self.library.add_book("Brave New World")
        self.assertTrue(self.library.is_book_available("Brave New World"))

    def test_borrow_all_books(self):
        self.library.borrow_book("The Great Gatsby")
        self.library.borrow_book("1984")
        self.assertFalse(self.library.is_book_available("The Great Gatsby"))
        self.assertFalse(self.library.is_book_available("1984"))

    def test_return_unborrowed_book(self):
        result = self.library.return_book("The Great Gatsby")
        self.assertFalse(result)

    def test_check_availability_non_existent_book(self):
        self.assertFalse(self.library.is_book_available("Non-existent Book"))

if __name__ == '__main__':
    unittest.main()
