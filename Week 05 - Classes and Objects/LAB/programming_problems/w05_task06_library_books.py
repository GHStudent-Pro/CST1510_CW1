# Task 6: Library Books


class Book:
    """A library book that can be borrowed and returned."""

    def __init__(self, title, author, is_available=True):
        """Store the book details on the object."""
        self.title = title
        self.author = author
        self.is_available = is_available

    def borrow(self):
        """Borrow the book if it is available; return True if it worked."""
        if not self.is_available:
            print(f"'{self.title}' is already borrowed.")
            return False
        self.is_available = False
        print(f"You borrowed '{self.title}'.")
        return True

    def return_book(self):
        """Mark the book as available again."""
        self.is_available = True


books = [
    Book("1984", "George Orwell"),
    Book("Animal Farm", "George Orwell"),
    Book("Pride and Prejudice", "Jane Austen"),
    Book("The Hobbit", "J.R.R. Tolkien"),
]

# 1. Borrow one book, then try again
books[0].borrow()
books[0].borrow()

# 2. Available books
print("\nAvailable books:")
for book in books:
    if book.is_available:
        print(f"  {book.title} by {book.author}")

# 3. Search by author
author = input("\nSearch for an author: ").strip().lower()
matches = [book for book in books if author in book.author.lower()]
if matches:
    for book in matches:
        print(f"  {book.title}")
else:
    print("  No books by that author.")
