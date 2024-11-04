class Book:
    def __init__(self, title, author):
        # Initialize the book with title, author, and availability (set to True by default)
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        # Return a string representation of the book including its availability status
        status = 'Available' if self.available else 'Not Available'
        return f"'{self.title}' by {self.author} [{status}]"


class Library:
    def __init__(self):
        # Initialize the library with an empty collection of books and a dictionary to track borrowed books
        self.collection = []
        self.borrowed_books = {}

    def add_book(self, title, author):
        # Add a new book to the library's collection
        new_book = Book(title, author)
        self.collection.append(new_book)
        print(f"Book '{title}' added to the library.")

    def view_books(self):
        # Display all the books in the library, including their availability
        if len(self.collection) == 0:
            print("No books in the library.")
        else:
            for book in self.collection:
                print(book)

    def borrow_book(self, user, book_title):
        # Allow a user to borrow a book if it is available
        for book in self.collection:
            if book.title.lower() == book_title.lower():
                if book.available:
                    book.available = False
                    self.borrowed_books[book.title] = user.name
                    print(f"'{book.title}' has been borrowed by {user.name}.")
                    return
                else:
                    print(f"Sorry, '{book.title}' is already borrowed.")
                    return
        print(f"Book '{book_title}' not found in the library.")

    def return_book(self, user, book_title):
        # Allow a user to return a borrowed book, making it available again
        if book_title in self.borrowed_books and self.borrowed_books[book_title] == user.name:
            for book in self.collection:
                if book.title == book_title:
                    book.available = True
                    del self.borrowed_books[book_title]
                    print(f"'{book.title}' has been returned by {user.name}.")
                    return
        else:
            print(f"Either the book '{book_title}' was not borrowed by {user.name} or it's not borrowed.")

    def view_borrowed_books(self):
        # Display all books that are currently borrowed along with the borrower's name
        if len(self.borrowed_books) == 0:
            print("No books are currently borrowed.")
        else:
            for book, borrower in self.borrowed_books.items():
                print(f"'{book}' is borrowed by {borrower}")


class User:
    def __init__(self, name):
        # Initialize the user with a name
        self.name = name

    def borrow_book(self, library, book_title):
        # Allow the user to borrow a book from the library
        library.borrow_book(self, book_title)

    def return_book(self, library, book_title):
        # Allow the user to return a book to the library
        library.return_book(self, book_title)


class Admin(User):
    def __init__(self):
        # Initialize the admin with a hardcoded name "Admin"
        super().__init__("Admin")

    def add_book(self, library, title, author):
        # Allow the admin to add a new book to the library
        library.add_book(title, author)

    def view_borrowed_books(self, library):
        # Allow the admin to view all borrowed books and who borrowed them
        library.view_borrowed_books()


def user_menu(library, user_name):
    """Displays the user menu and handles user operations."""
    # Create a user with the provided name and display the menu for user operations
    user = User(user_name)
    while True:
        print(f"\n--- User Menu (Logged in as: {user.name}) ---")
        print("1. View available books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Exit to main menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            # View available books
            library.view_books()

        elif choice == '2':
            # Borrow a book
            book_title = input("Enter the title of the book to borrow: ")
            user.borrow_book(library, book_title)

        elif choice == '3':
            # Return a book
            book_title = input("Enter the title of the book to return: ")
            user.return_book(library, book_title)

        elif choice == '4':
            # Exit to the main menu
            print("Exiting to main menu.")
            break

        else:
            print("Invalid choice. Please try again.")


def admin_menu(library):
    """Displays the admin menu and handles admin operations."""
    # Create an admin and display the menu for admin operations
    admin = Admin()
    while True:
        print(f"\n--- Admin Menu (Logged in as: {admin.name}) ---")
        print("1. Add a new book")
        print("2. View all books")
        print("3. View borrowed books")
        print("4. Exit to main menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            # Admin adds a new book
            book_title = input("Enter the title of the new book: ")
            book_author = input("Enter the author of the new book: ")
            admin.add_book(library, book_title, book_author)

        elif choice == '2':
            # View all books in the library
            library.view_books()

        elif choice == '3':
            # View all borrowed books
            admin.view_borrowed_books(library)

        elif choice == '4':
            # Exit to the main menu
            print("Exiting to main menu.")
            break

        else:
            print("Invalid choice. Please try again.")


def main():
    # Initialize the library system and set the admin password
    library = Library()
    admin_password = "admin123"

    # Add some test books to the library
    library.add_book("1984", "George Orwell")
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
    library.add_book("Moby Dick", "Herman Melville")
    library.add_book("War and Peace", "Leo Tolstoy")

    # Main loop to display the main menu (User/Admin selection)
    while True:
        print("\n--- Welcome to the Library System! ---")
        print("1. I am a User")
        print("2. I am an Admin")
        print("3. Exit")
        choice = input("Are you a User or Admin (or Exit)? Enter your choice: ")

        if choice == '1':
            # User menu
            user_name = input("Enter your name: ")
            user_menu(library, user_name)

        elif choice == '2':
            # Admin menu, after verifying password
            admin_pass = input("Enter admin password: ")
            if admin_pass == admin_password:
                admin_menu(library)
            else:
                print("Unauthorized access. Incorrect admin password.")

        elif choice == '3':
            # Exit the system
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
