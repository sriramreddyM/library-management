# check_ins = []
# check_outs = []

# def checkout_book(user_id, isbn):
#     check_outs.append({"user_id": user_id, "isbn": isbn})

# def checkin_book(user_id, isbn):
#     check_ins.append({"user_id": user_id, "isbn": isbn})

from book import Books

class Record:
    """
    Represents a record manager for tracking book check-in and check-out actions.
    """
    def __init__(self, book_management: Books) -> None:
        """
        Initializes a Record object with a reference to the Books.

        Args:
        - book_management (Books): An instance of the Books.
        """
        self.records = []
        self.check_outs = []
        self.check_ins = []
        self.book_management = book_management

    def checkout_book(self, user_id, isbn):
        """
        Checks out a book for a user.

        Args:
        - user_id (str): The ID of the user checking out the book.
        - isbn (str): The ISBN of the book to be checked out.

        Returns:
        - None
        """
        for book in self.book_management.books:
            if str(book.isbn) == str(isbn):
                if book.qty > 0:
                    book.qty -= 1
                    self.check_outs.append({"user_id": user_id, "isbn": isbn})
                    self.records.append({"user_id": user_id, "isbn": isbn, "action": "checkout"})
                    print("Book checked out successfully.")
                    # Future expansion: due dates for books
                else:
                    print("Sorry, book is not available for checkout")
                return
        print("Book not found")
        

    def checkin_book(self, user_id, isbn):
        """
        Checks in a book previously checked out by a user.

        Args:
        - user_id (str): The ID of the user checking in the book.
        - isbn (str): The ISBN of the book to be checked in.

        Returns:
        - None
        """
        if {"user_id": user_id, "isbn": isbn} not in self.check_outs:
            print("Cannot check in. No corresponding checkout record found.")
            return
        for book in self.book_management.books:
            if str(book.isbn) == str(isbn):
                book.qty += 1
                self.check_ins.append({"user_id": user_id, "isbn": isbn})
                self.records.append({"user_id": user_id, "isbn": isbn, "action": "checkin"})
                print("Book checked in successfully")
                # Future expansion: late fees for overdue books 
                return
    print("Book not found")