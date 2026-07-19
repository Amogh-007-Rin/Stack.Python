"""Module 050: Milestone Project — Library/Inventory Management System.

Implement all classes below following the docstrings and specifications.
Run this file to test your implementation.
"""


# ---------- Book Class ----------

class Book:
    """Represents a book in the library.

    TODO: Implement __init__, borrow(), return_copy(), @property for
    available and copies, __str__, __repr__, __eq__, __hash__.
    """

    def __init__(self, title, author, isbn, copies=1):
        """Initialize a Book instance.

        Args:
            title: The book title.
            author: The book author.
            isbn: The ISBN identifier.
            copies: Total number of copies (default 1).
        """
        # TODO: set instance attributes
        pass

    @property
    def available(self):
        """int: Number of copies available for borrowing."""
        # TODO: implement
        pass

    @property
    def copies(self):
        """int: Total number of copies owned."""
        # TODO: implement
        pass

    def borrow(self):
        """Borrow one copy.

        Returns:
            True if a copy was available, False otherwise.
        """
        # TODO: implement
        pass

    def return_copy(self):
        """Return one copy.

        Returns:
            True if a copy was returned, False if all were already available.
        """
        # TODO: implement
        pass

    def __str__(self):
        """Return user-friendly string: 'title by author'."""
        # TODO: implement
        pass

    def __repr__(self):
        """Return unambiguous string recreating the object."""
        # TODO: implement
        pass

    def __eq__(self, other):
        """Check equality by ISBN."""
        # TODO: implement
        pass

    def __hash__(self):
        """Hash based on ISBN."""
        # TODO: implement
        pass


# ---------- Member Classes ----------

class Member:
    """Base member class.

    TODO: Implement __init__, can_borrow(), borrow_book(), return_book(),
    borrowing_limit, loan_period_days, __str__, __repr__.
    """

    def __init__(self, name, member_id):
        """Initialize a Member.

        Args:
            name: The member's name.
            member_id: Unique identifier.
        """
        # TODO: set instance attributes
        pass

    @property
    def borrowing_limit(self):
        """int: Maximum books that can be borrowed."""
        return 0

    @property
    def loan_period_days(self):
        """int: Loan period in days."""
        return 0

    def can_borrow(self):
        """Check if member can borrow more books.

        Returns:
            True if under the borrowing limit.
        """
        # TODO: implement
        pass

    def borrow_book(self, book):
        """Add book to borrowed list.

        Args:
            book: The Book to borrow.

        Raises:
            RuntimeError: If at borrowing limit.
        """
        # TODO: implement
        pass

    def return_book(self, book):
        """Remove book from borrowed list.

        Args:
            book: The Book to return.

        Raises:
            ValueError: If book was not borrowed by this member.
        """
        # TODO: implement
        pass

    def __str__(self):
        """Return 'name (ID: member_id)'."""
        # TODO: implement
        pass

    def __repr__(self):
        """Return unambiguous representation."""
        # TODO: implement
        pass


class StudentMember(Member):
    """Student member with 3-book limit and 14-day loan period."""

    @property
    def borrowing_limit(self):
        return 3

    @property
    def loan_period_days(self):
        return 14


class TeacherMember(Member):
    """Teacher member with 10-book limit and 30-day loan period."""

    @property
    def borrowing_limit(self):
        return 10

    @property
    def loan_period_days(self):
        return 30


# ---------- Library Class ----------

class Library:
    """Manages books and members.

    TODO: Implement __init__, add_book(), add_member(), borrow_book(),
    return_book(), list_books(), list_members(), __str__, __len__.
    """

    def __init__(self, name):
        """Initialize a Library.

        Args:
            name: The library name.
        """
        # TODO: set instance attributes
        pass

    def add_book(self, book):
        """Add a book to the collection.

        Args:
            book: A Book instance.
        """
        # TODO: implement
        pass

    def add_member(self, member):
        """Register a member.

        Args:
            member: A Member instance.
        """
        # TODO: implement
        pass

    def borrow_book(self, member_id, isbn):
        """Borrow a book for a member.

        Args:
            member_id: The member's ID.
            isbn: The book's ISBN.

        Raises:
            ValueError: If member or book not found.
            RuntimeError: If no copies available or limit reached.
        """
        # TODO: implement
        pass

    def return_book(self, member_id, isbn):
        """Return a borrowed book.

        Args:
            member_id: The member's ID.
            isbn: The book's ISBN.

        Raises:
            ValueError: If member or book not found.
        """
        # TODO: implement
        pass

    def list_books(self):
        """Print all books with availability."""
        # TODO: implement
        pass

    def list_members(self):
        """Print all members and their borrowed book count."""
        # TODO: implement
        pass

    def __str__(self):
        """Return 'Library: name'."""
        # TODO: implement
        pass

    def __len__(self):
        """Return number of books."""
        # TODO: implement
        pass


# ---------- Demo / Test ----------

def main():
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
        lib.borrow_book("S001", "004")
    except RuntimeError as e:
        print(f"  Error: {e}")

    print("\nAll tests passed! Your library system is working.")


if __name__ == "__main__":
    main()
