class BookNotAvailableException(Exception):
    def __init__(self, book_title):
        self.book_title = book_title
        self.message = self.create_error_message(book_title)
        super().__init__(self.message)

    @staticmethod
    def create_error_message(book_title):
        return f"The book '{book_title}' is not available for checkout."

    def get_book_title(self):
        return self.book_title


class LibrarySystem:
    def __init__(self):
        self.available_books = {"Harry Potter": 1, "1984": 0}  # Simplified inventory

    def is_book_available(self, book_title):
        return self.available_books.get(book_title, 0) > 0

    def checkout_book(self, book_title):
        if not self.is_book_available(book_title):
            raise BookNotAvailableException(book_title)
        self.available_books[book_title] -= 1
        print(f"Book '{book_title}' checked out successfully.")


if __name__ == "__main__":
    library = LibrarySystem()

    try:
        book_title = "Harry Potter"
        library.checkout_book(book_title)
    except BookNotAvailableException as e:
        print(e)  # Outputs: The book '1984' is not available for checkout.
