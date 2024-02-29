import os
import csv
from book import Books
from  user import Users
from check import Record

class Storage:
    """
    File based storage management for books, users, and records.
    """
    def __init__(self, books_storage: str, users_storage: str, records_storage: str, 
                 books_management: Books, users_management: Users, records_management: Record) -> None:
        """
        Initializes the Storage manager with file paths and management instances.

        Args:
        - books_storage (str): Path to the file storing book data.
        - users_storage (str): Path to the file storing user data.
        - records_storage (str): Path to the file storing record data.
        - books_management (Books): Instance of the Books.
        - users_management (Users): Instance of the Users.
        - records_management (Record): Instance of the Record.
        """

        self.books_storage = books_storage
        self.users_storage = users_storage
        self.records_storage = records_storage
        self.books_management = books_management
        self.users_management = users_management
        self.records_management = records_management
    
    def read_books(self):
        """Reads and populates the books from the file storage"""
        if os.path.isfile(self.books_storage):
            with open(self.books_storage, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    title, author, isbn, qty = row
                    self.books_management.add_book(title, author, int(isbn), int(qty))

    def read_users(self):
        """Reads and populates the users from the file storage"""
        if os.path.isfile(self.users_storage):
            with open(self.users_storage, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    name, user_id = row
                    self.users_management.add_user(name, user_id)

    def read_records(self):
        """Reads and populates the records from the file storage""" 
        if os.path.isfile(self.records_storage):
            with open(self.records_storage, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    user_id, isbn, action = row
                    if action == 'checkout':
                        self.records_management.checkout_book(user_id, isbn)
                    elif action == 'checkin':
                        self.records_management.checkin_book(user_id, isbn)

    def write_books(self):
        """Writes books data from Books management to file storage"""
        with open(self.books_storage, 'w', newline='') as file:
            writer = csv.writer(file)
            for book in self.books_management.books:
                writer.writerow([book.title, book.author, book.isbn, book.qty])

    def write_users(self):
        """Writes users data from Users management to file storage"""
        with open(self.users_storage, 'w', newline='') as file:
            writer = csv.writer(file)
            for user in self.users_management.users:
                writer.writerow([user.name, user.user_id])

    def write_records(self):
        """Writes recirds data from Records management to file storage"""
        with open(self.records_storage, 'w', newline='') as file:
            writer = csv.writer(file)
            for record in self.records_management.records:
                writer.writerow([record['user_id'], record['isbn'], record['action']])
    
    def load(self):
        """Loads the from file storages into repective models"""
        self.read_books()
        self.read_users()
        self.read_records()

    def save(self):
        """Saves the data from repective models to file storages"""
        self.write_books()
        self.write_users()
        self.write_records()