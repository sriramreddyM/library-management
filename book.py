class Book:
    """
    Represents a book with basic attributes, title, author, ISBN, and quantity
    """
    def __init__(self, title: str, author: str, isbn: int, qty: int=0) -> None:
        """
        Initialize a Book object with the given attributes,

        Args:
        - title (str): title of the book.
        - author (str): author of the book.
        - isbn (int): the ISBN number of the book.
        - qty (int): quantity of the book available (default is 0).
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.qty = qty

    
    def __str__(self) -> str:
        """
        returns a string representation of the Book object.
        """
        return f"{self.title} by {self.author} ISBN no: {self.isbn}"

    def __eq__(self, book) -> bool:
        """
        compares two Book objects to check if they same by attributes

        Args:
        - other (Book): The other Book object to compare

        Returns:
        - bool: True if the books are same, False otherwise.
        """
        if isinstance(book, Book):
            return (self.title == book.title and
                    self.author == book.author and
                    self.isbn == book.isbn)
        return False
    
class Books:
    """
    Represents a collection of Book objects.
    """
    def __init__(self) -> None:
        """
        Initializes a Books object with an empty list to store books (Object instances of Book class).
        """
        self.books = []

    def add_book(self, title: str, author: str, isbn: int, qty: int):
        """
        Adds a new book to the collection

        Args:
        - title (str): title of the book.
        - author (str): author of the book.
        - isbn (int): the ISBN number of the book.
        - qty (int): quantity of the book available.

        Returns:
        - None
        """
        book = Book(title, author, isbn, qty)
        self.books.append(book)

    def update_book(self, title: str=None, author: str=None, isbn: int=None, new_title: str=None, new_author: str=None, new_isbn: int=None) -> dict:
        """
        Updates details of a book in the collection

        Args:
        - title (str): title of the book to update
        - author (str): author of the book to update
        - isbn (int): The ISBN of the book to update
        - new_title (str): new title for the book
        - new_author (str): new author for the book
        - new_isbn (int): The nwe ISBN for the book.

        Returns:
        - dict: A dictionary showing the status of the update and the updated book details.
        """

        checking_book = Book(title, author, isbn)
        is_updated = False
        for book in self.books:
            if checking_book.__eq__(book):
                book.title = new_title
                book.author = new_author
                book.isbn = new_isbn
                is_updated = True
        
        return {"status": is_updated, "Updated book": vars(book)}
    
    def delete_book(self, title: str=None, author: str=None, isbn: int=None) -> dict:
        """
        Deletes a book from the collection.

        Args:
        - title (str): title of the book to delete.
        - author (str): author of the book to delete.
        - isbn (int): The ISBN of the book to delete.

        Returns:
        - dict: A dictionary showing the status of the deletion and the deleted book details.
        """
        checking_book = Book(title, author, isbn)
        is_deleted = False
        for listed_book in self.books:
            if checking_book.__eq__(listed_book):
                self.books.remove(listed_book)
                is_deleted =True

        return {"status": is_deleted, "Deleted book": vars(checking_book)}

    def list_books(self):
        """
        Prints all books with details in the collection.
        """
        for book in self.books:
            print(vars(book))

    def search_by_title(self, title: str) -> list:
        """
        Seaches books collection by title.

        Args:
        - title (str): title of the book to search for.

        Returns:
        - list: list of dictionaries containing details of books which matches with the title.
        """
        return [vars(book) for book in self.books if book.title == title]

    def search_by_author(self, author: str) -> list:
        """
        Seaches books collection by author.

        Args:
        - author (str): author of the book to search for.

        Returns:
        - list: list of dictionaries containing details of books which matches the author.
        """
        return [vars(book) for book in self.books if book.author == author]

    def search_by_isbn(self, isbn: int) -> list:
        """
        Seaches books collection by ISBN.

        Args:
        - isbn (int): The ISBN of the book to search for.

        Returns:
        - list: list of dictionaries containing details of books which matches the ISBN.
        """
        return [vars(book) for book in self.books if int(book.isbn) == int(isbn)]

    # def track_book(self, isbn: int) -> str:
    #     """
    #     Tracks status of a booki n the collection.

    #     Args:
    #     - isbn (int): The ISBN of the book to track.

    #     Returns:
    #     - str: string represantion of the status of the book
    #     """
    #     book = self.search_by_isbn(isbn)
    #     if len(book) > 0:
    #         if book['qty'] > 0:
    #             print(f"{book['title']} by {book['author']} ISBN: {book['isbn']}, Quantity available: {book['qty']}")
    #         else:
    #             print(f"{book['title']} by {book['author']} ISBN: {book['isbn']}, Not available.")
    #     else:
    #         print("No book found with given ISBN")