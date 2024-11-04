import unittest

from CSF101_CAP2_02230292 import Library, Admin, User
class TestLibrarySystem(unittest.TestCase):
    def setUp(self):
        # Create a library and admin user for tests
        self.library = Library()
        self.admin = Admin()
        self.user = User("Alice")

        # Add some test books
        self.library.add_book("1984", "George Orwell")
        self.library.add_book("To Kill a Mockingbird", "Harper Lee")
    
    def test_valid_book_borrowing(self):
        # Test if a user can successfully borrow a book
        self.user.borrow_book(self.library, "1984")
        borrowed_book = next(book for book in self.library.collection if book.title == "1984")
        self.assertFalse(borrowed_book.available)
        self.assertIn("1984", self.library.borrowed_books)
        self.assertEqual(self.library.borrowed_books["1984"], "Alice")

    def test_invalid_book_borrowing(self):
        # Borrow a book and attempt to borrow it again to test invalid borrowing
        self.user.borrow_book(self.library, "1984")
        self.user.borrow_book(self.library, "1984")  # Attempting to borrow the same book again
        borrowed_book = next(book for book in self.library.collection if book.title == "1984")
        self.assertFalse(borrowed_book.available)
        self.assertEqual(self.library.borrowed_books["1984"], "Alice")

    def test_valid_book_returning(self):
        # Test if a user can successfully return a borrowed book
        self.user.borrow_book(self.library, "1984")
        self.user.return_book(self.library, "1984")
        returned_book = next(book for book in self.library.collection if book.title == "1984")
        self.assertTrue(returned_book.available)
        self.assertNotIn("1984", self.library.borrowed_books)

    def test_invalid_book_returning(self):
        # Test returning a book that hasn't been borrowed
        self.user.return_book(self.library, "1984")  # Book was not borrowed
        returned_book = next(book for book in self.library.collection if book.title == "1984")
        self.assertTrue(returned_book.available)  # Ensure the book is still marked as available

    def test_admin_adding_books(self):
        # Test if the admin can add books and they appear in the library collection
        self.admin.add_book(self.library, "The Great Gatsby", "F. Scott Fitzgerald")
        added_book = next(book for book in self.library.collection if book.title == "The Great Gatsby")
        self.assertEqual(added_book.title, "The Great Gatsby")
        self.assertEqual(added_book.author, "F. Scott Fitzgerald")
        self.assertTrue(added_book.available)

    def test_borrow_all_books(self):
        # Borrow all books and check if their availability changes
        for book in self.library.collection:
            self.user.borrow_book(self.library, book.title)
        for book in self.library.collection:
            self.assertFalse(book.available)  # All books should now be unavailable

    def test_return_unborrowed_book(self):
        # Test returning a book that was not borrowed to see if it handles gracefully
        self.user.return_book(self.library, "To Kill a Mockingbird")  # Should not affect availability
        unborrowed_book = next(book for book in self.library.collection if book.title == "To Kill a Mockingbird")
        self.assertTrue(unborrowed_book.available)  # Book should still be marked as available


if __name__ == "__main__":
    unittest.main()
