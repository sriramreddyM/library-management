#main.py
from book import Books
from  user import Users
from check import Record
from storage import Storage
import datetime

book_management = Books()
user_management = Users()
record_management = Record(book_management)

storage_management = Storage('storage/books.csv', 'storage/users.csv', 'storage/records.csv', book_management, user_management, record_management)
storage_management.load()

class Logger:
    def __init__(self, log_file='storage/library_app.log'):
        self.log_file = log_file

    def log(self, msg):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, 'a+') as file:
            file.write(f"[{timestamp}] {msg}\n")

logger = Logger()

def add_book():
    print("Please give the details of the book to add \n")
    title = input("Enter title: ")
    author = input("Enter author: ")
    isbn = input("Enter ISBN: ")
    qty = input("Enter number of quantity:")
    book_management.add_book(title, author, isbn, qty)
    storage_management.save()
    logger.log(f"Added a new book: {title} by {author}, ISBN: {isbn}, Quantity: {qty}")

def search_book():
    print("1. to search by title")    
    print("2. to search by isbn")
    choice = input("select to search")
    if choice == "1":
        title = input("ENter book title")
        book = book_management.search_by_title(title)
        print(book)
        logger.log(f"Searched for book by title: {title}")
    elif choice == "2":
        isbn = input("ENtyer ISBN: ")
        book = book_management.search_by_isbn(isbn)
        print(book)
        logger.log(f"Searched for book by isbn: {isbn}")


def update_book():
    print("Please give present details of the book \n")
    title = input("Enter title")
    author = input("Enter author: ")
    isbn = input("Enter ISBN: ")
    new_title = input("Enter New title")
    new_author = input("Enter New author: ")
    new_isbn = input("Enter New ISBN: ")
    book_management.update_book(title, author, isbn, new_title, new_author, new_isbn)
    storage_management.save()
    logger.log(f"Updated book: {new_title} by {new_author}, ISBN: {new_isbn}")


def delete_book():
    print("Please give details of the book to delete \n")
    title = input("Enter title")
    author = input("Enter author: ")
    isbn = input("Enter ISBN: ")
    book_management.delete_book(title, author, isbn)
    storage_management.save()
    logger.log(f"Deleted book: {title}")


def add_user():
    name = input("Enter user name: ")
    user_id = input("Enter user ID: ")
    user_management.add_user(name, user_id)
    storage_management.save()
    logger.log(f"Added user name: {name}, user_id {user_id}")


def search_user():
    print("To search user \n")
    print("1. by name")
    print("2. by user_id")
    choice = input("please select")
    if choice == "1":
        search_name = input("user name: ")
        user = user_management.search_by_name(search_name)
        print(user)
        logger.log(f"Searched for user by name: {search_name}")
    elif choice == "2":
        search_user_id = input("user id: ")
        user = user_management.search_by_id(search_user_id)
        print(user)
        logger.log(f"Searched for user by id: {search_user_id}")
    else:
        print("please select a valid choice")
        search_user()

def delete_user():
    print("Please give details of the user to delete \n")
    user_id = input("Enter user_id: ")
    user_management.delete_user(user_id)
    storage_management.save()
    logger.log(f"Deleted user: {user_id}")


def checkout_book():
    user_id = input("Enter user ID: ")
    isbn = input("Enter ISBN of the book to checkout: ")
    record_management.checkout_book(user_id, isbn)
    storage_management.save()
    logger.log("Tried Book ISBN: {isbn} checkout by user: {user_id}")

def checkin_book():
    user_id = input("Enter user ID: ")
    isbn = input("Enter ISBN of the book to checkout: ")
    record_management.checkin_book(user_id, isbn)
    storage_management.save()
    logger.log("Tried Book ISBN: {isbn} checkin by user: {user_id}")


def go_back():
    pass
 
# actions = {'1': add_book, '2': book_management.list_books, '3': update_book, '4': delete_book, '5': add_user, '6': user_management.list_users, '7': checkout_book, '8': checkin_book, '9': exit()}
operations = {
    '1': {
        '1': add_book, 
        '2': book_management.list_books, 
        '3': search_book,
        '4': update_book, 
        '5': delete_book,
        '6': go_back
    },
    '2': {
        '1': add_user, 
        '2': user_management.list_users,
        '3': search_user,
        '4': delete_user,
        '5': go_back
    },
    '3': {
        '1': checkout_book, 
        '2': checkin_book,
        '3': go_back
    },
    '4': exit
}

main_card = {
    '1': 'Add/Update/Search/Delete a Book',
    '2': 'Add/Search/Delete a User',
    '3': 'Check_in / Check_out a book',
    '4': 'exit the app' # this is never called
}

second_card = {
    '1': {
        '1': "Add a Book", 
        '2': "List books", 
        '3': "Search for a Book",
        '4': "update a Book", 
        '5': "delete a Book",
        '6': "go back"
    },
    '2': {
        '1': "Add a user", 
        '2': "List users",
        '3': "search a user",
        '4': "delete a user",
        '5': "go back"
    },
    '3': {
        '1': "checkout book", 
        '2': "checkin book",
        '3': "go back"
    },
    '4': "Back to main card"
}

def save_status():
    pass

def menu():
    print("\nLibrary Management System")
    for key, op in main_card.items():
        print(f"{key} for {op}")
    choice = input("Enter choice: ")
    if choice == "4":
        save_status()
        exit()
    if choice in main_card.keys():
        for sec_key, sec_op in second_card[choice].items():
            print(f"{sec_key} for {sec_op}")
        sec_choice = input("Enter choice: ")
        if sec_choice in second_card[choice].keys():
            status = operations[choice][sec_choice]()
            if status:
                print(status)
        else:
            print("Please select a valid operation")
    else:
        print("Please select a valid operation")
        
        
def main():
    while True:
        menu()

if __name__ == "__main__":
    main()
