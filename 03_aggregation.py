"""Aggregation (Weak Has-a): child objects exist independently and are passed in."""


class Book:
    def __init__(self, title: str):
        self.title = title

    def __del__(self):
        print(f"Book object destroyed: '{self.title}'")


class Library:
    def __init__(self, books: list = None):
        # The Library accepts already-existing Book objects
        self.books = books if books else []

    def __del__(self):
        print("Library object destroyed.")


if __name__ == "__main__":
    # 1. Books are created outside first, so they exist even without a library
    book1 = Book("The Hobbit")
    book2 = Book("1984")

    # 2. Passed into the container class
    my_library = Library([book1, book2])
    print(f"Library populated with: {[b.title for b in my_library.books]}")

    print("\nExecuting: del my_library")
    del my_library  # Wipes out the library only

    print("\nChecking variable accessibility after container deletion:")
    print(f"Still active in memory -> book1: {book1.title}")
    print(f"Still active in memory -> book2: {book2.title}")
    # book1 and book2 live on after the Library is gone
