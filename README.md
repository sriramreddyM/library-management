# Library Management System (Techolution coding assignment)

A simple command-line based app for Library Management System.

## Features

- Add, update, delete, list, and search books by various attributes like title, author, or ISBN
- Add, update, delete, list, and search users by attributes like name or user ID
- Check-in and check-out books to users
- Simple logging of operations
- Data storage in CSV files for easy management
- Intuitive command-line interface


## Testing

- Clone the repo
- Run `main.py` script to start the app
- When the application starts, you will see a main menu with options to perform different operations
- Select an option and follow the prompts to complete the operation
- Data is saved automatically to CSV files after each operation
- Data is loaded automatically from CSV files when starting of the application

## File Structure

- `main.py`: Main script to run the Library Management System
- `book.py`: Defines the Book and Books classes for book management
- `user.py`: Defines the User and Users classes for user management
- `check.py`: Defines the Record class for managing book check-in and check-out records
- `storage.py`: Defines the Storage class for reading from and writing to CSV files
- `storage/`: Directory containing CSV files for storing book, user, and record data