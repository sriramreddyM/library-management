# Manage books (add, update, delete, list, and search by various attributes like title, author, or ISBN

class Book:
    def __init__(self, title: str, author: str, isbn: int, qty: int=0) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self.qty = qty

    
    def __str__(self) -> str:
        return f"{self.title} by {self.author} ISBN no: {self.isbn}"

    def __eq__(self, book):
        if isinstance(book, Book):
            return (self.title == book.title and
                    self.author == book.author and
                    self.isbn == book.isbn)
        return False
    
class Books:
    def __init__(self) -> None:
        self.books = []

    def add_book(self, title: str, author: str, isbn: int, qty: int):
        book = Book(title, author, isbn, qty)
        self.books.append(book)

    def update_book(self, title: str=None, author: str=None, isbn: int=None, new_title: str=None, new_author: str=None, new_isbn: int=None) -> dict:
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
        checking_book = Book(title, author, isbn)
        is_deleted = False
        for listed_book in self.books:
            if checking_book.__eq__(listed_book):
                self.books.remove(listed_book)
                is_deleted =True

        return {"status": is_deleted, "Deleted book": vars(checking_book)}

    def list_books(self):
        for book in self.books:
            print(vars(book))

    def search_by_title(self, title: str) -> list:
        return [vars(book) for book in self.books if book.title == title]

    def search_by_author(self, author: str) -> list:
        return [vars(book) for book in self.books if book.author == author]

    def search_by_isbn(self, isbn: int) -> list:
        return [vars(book) for book in self.books if int(book.isbn) == int(isbn)]

    def track_book(self, isbn: int):
        book = self.search_by_isbn(isbn)
        if len(book) > 0:
            if book['qty'] > 0:
                print(f"{book['title']} by {book['author']} ISBN: {book['isbn']}, Quantity available: {book['qty']}")
            else:
                print(f"{book['title']} by {book['author']} ISBN: {book['isbn']}, Not available.")
        else:
            print("No book found with given ISBN")