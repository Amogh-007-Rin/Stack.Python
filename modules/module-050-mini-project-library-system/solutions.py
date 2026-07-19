"""Module 050: Milestone Project — Library/Inventory Management System.

This module provides a complete OOP-based library management system
demonstrating concepts from Modules 041-049.
"""


class Book:
    """Represents a book in the library.

    Attributes:
        title: The title of the book.
        author: The author of the book.
        isbn: The ISBN identifier for the book.
        _copies: Total number of copies owned.
        _available: Number of copies currently available for borrowing.
    """

    def __init__(self, title, author, isbn, copies=1):
        """Initialize a Book instance.

        Args:
            title: The book title.
            author: The book author.
            isbn: The ISBN identifier.
            copies: Total number of copies (default 1).
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self._copies = copies
        self._available = copies

    @property
    def available(self):
        """int: Number of copies available for borrowing."""
        return self._available

    @property
    def copies(self):
        """int: Total number of copies owned."""
        return self._copies

    def borrow(self):
        """Borrow one copy of this book.

        Returns:
            True if a copy was available and borrowed, False otherwise.
        """
        if self._available <= 0:
            return False
        self._available -= 1
        return True

    def return_copy(self):
        """Return one copy of this book.

        Returns:
            True if a copy was successfully returned, False if all copies
            were already available.
        """
        if self._available < self._copies:
            self._available += 1
            return True
        return False

    def __str__(self):
        """Return a user-friendly string representation."""
        return f"{self.title} by {self.author}"

    def __repr__(self):
        """Return an unambiguous string representation."""
        return f"Book({self.title!r}, {self.author!r}, {self.isbn!r}, {self._copies})"

    def __eq__(self, other):
        """Check equality based on ISBN."""
        if not isinstance(other, Book):
            return NotImplemented
        return self.isbn == other.isbn

    def __hash__(self):
        """Hash based on ISBN."""
        return hash(self.isbn)


class Member:
    """Represents a library member.

    Attributes:
        name: The member's name.
        member_id: Unique identifier for the member.
        borrowed_books: List of books currently borrowed.
    """

    def __init__(self, name, member_id):
        """Initialize a Member instance.

        Args:
            name: The member's name.
            member_id: Unique identifier.
        """
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    @property
    def borrowing_limit(self):
        """int: Maximum number of books that can be borrowed at once."""
        return 0

    @property
    def loan_period_days(self):
        """int: Number of days a book can be borrowed."""
        return 0

    def can_borrow(self):
        """Check if the member can borrow more books.

        Returns:
            True if under the borrowing limit, False otherwise.
        """
        return len(self.borrowed_books) < self.borrowing_limit

    def borrow_book(self, book):
        """Add a book to the member's borrowed list.

        Args:
            book: The Book instance to borrow.

        Raises:
            RuntimeError: If the member has reached the borrowing limit.
        """
        if not self.can_borrow():
            raise RuntimeError(
                f"{self.name} has reached the borrowing limit "
                f"of {self.borrowing_limit}"
            )
        self.borrowed_books.append(book)

    def return_book(self, book):
        """Remove a book from the member's borrowed list.

        Args:
            book: The Book instance to return.

        Raises:
            ValueError: If the book was not borrowed by this member.
        """
        if book not in self.borrowed_books:
            raise ValueError(f"{self.name} did not borrow {book.title}")
        self.borrowed_books.remove(book)

    def __str__(self):
        """Return a user-friendly string representation."""
        return f"{self.name} (ID: {self.member_id})"

    def __repr__(self):
        """Return an unambiguous string representation."""
        return f"{type(self).__name__}({self.name!r}, {self.member_id!r})"


class StudentMember(Member):
    """A library member who is a student with a 3-book limit."""

    @property
    def borrowing_limit(self):
        return 3

    @property
    def loan_period_days(self):
        return 14


class TeacherMember(Member):
    """A library member who is a teacher with a 10-book limit."""

    @property
    def borrowing_limit(self):
        return 10

    @property
    def loan_period_days(self):
        return 30


class Library:
    """Manages a collection of books and members.

    Attributes:
        name: The name of the library.
        _books: Dict mapping ISBN to Book objects.
        _members: Dict mapping member_id to Member objects.
    """

    def __init__(self, name):
        """Initialize a Library instance.

        Args:
            name: The name of the library.
        """
        self.name = name
        self._books = {}
        self._members = {}

    def add_book(self, book):
        """Add a book to the library's collection.

        Args:
            book: A Book instance to add.
        """
        self._books[book.isbn] = book

    def add_member(self, member):
        """Register a member with the library.

        Args:
            member: A Member instance to register.
        """
        self._members[member.member_id] = member

    def borrow_book(self, member_id, isbn):
        """Allow a member to borrow a book.

        Args:
            member_id: The member's identifier.
            isbn: The book's ISBN.

        Raises:
            ValueError: If the member or book is not found.
            RuntimeError: If no copies are available or limit reached.
        """
        member = self._members.get(member_id)
        book = self._books.get(isbn)

        if not member:
            raise ValueError(f"No member with ID {member_id}")
        if not book:
            raise ValueError(f"No book with ISBN {isbn}")

        if not book.borrow():
            raise RuntimeError(f"No copies of {book.title} available")

        member.borrow_book(book)

    def return_book(self, member_id, isbn):
        """Process a book return.

        Args:
            member_id: The member's identifier.
            isbn: The book's ISBN.

        Raises:
            ValueError: If the member or book is not found, or the book
                was not borrowed by this member.
        """
        member = self._members.get(member_id)
        book = self._books.get(isbn)

        if not member:
            raise ValueError(f"No member with ID {member_id}")
        if not book:
            raise ValueError(f"No book with ISBN {isbn}")

        member.return_book(book)
        book.return_copy()

    def list_books(self):
        """Print all books in the library with availability status."""
        for book in self._books.values():
            status = f"({book.available}/{book.copies} available)"
            print(f"  {book} {status}")

    def list_members(self):
        """Print all registered members with their borrowed book count."""
        for member in self._members.values():
            borrowed = len(member.borrowed_books)
            print(f"  {member} - {borrowed} books borrowed")

    def __str__(self):
        """Return a user-friendly string representation."""
        return f"Library: {self.name}"

    def __len__(self):
        """Return the number of books in the library."""
        return len(self._books)


def demo():
    """Run a demonstration of the library system."""
    lib = Library("City Central Library")

    lib.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "001", 3))
    lib.add_book(Book("1984", "George Orwell", "002", 2))
    lib.add_book(Book("To Kill a Mockingbird", "Harper Lee", "003", 1))
    lib.add_book(Book("Python 101", "Alice Smith", "004", 5))

    lib.add_member(StudentMember("Alice Johnson", "S001"))
    lib.add_member(StudentMember("Bob Williams", "S002"))
    lib.add_member(TeacherMember("Dr. Carol Davis", "T001"))

    print(f"Welcome to {lib}")
    print(f"Total books: {len(lib)}\n")

    print("Initial state:")
    lib.list_books()
    print()
    lib.list_members()
    print()

    print("Alice borrows 'The Great Gatsby'...")
    lib.borrow_book("S001", "001")
    print("Bob borrows 'The Great Gatsby' and '1984'...")
    lib.borrow_book("S002", "001")
    lib.borrow_book("S002", "002")
    print("Dr. Carol borrows 'Python 101' and 'To Kill a Mockingbird'...")
    lib.borrow_book("T001", "004")
    lib.borrow_book("T001", "003")
    print()

    print("After borrowing:")
    lib.list_books()
    print()
    lib.list_members()
    print()

    print("Bob returns '1984'...")
    lib.return_book("S002", "002")
    print()

    print("After return:")
    lib.list_books()
    print()
    lib.list_members()
    print()

    print("Attempting to borrow beyond limit (Alice tries 4th book)...")
    try:
        lib.borrow_book("S001", "004")
        lib.borrow_book("S001", "004")
        lib.borrow_book("S001", "004")
        lib.borrow_book("S001", "004")  # should fail
    except RuntimeError as e:
        print(f"  Error: {e}")

    print("\nDemo complete!")


if __name__ == "__main__":
    demo()
