#Manage users (add, update, delete, list, and search by attributes like name, user ID

class User:
    """
    Represents a user with attributes such as name and user ID.
    """
    def __init__(self, name: str, user_id: str):
        """
        Initializes a User object with the given attributes.

        Args:
        - name (str): name of the user.
        - user_id (str): The ID of the user.
        """
        self.name = name
        self.user_id = user_id
    
    def __str__(self) -> str:
        """
        Returns a string representation of the User object.
        """
        return f"Name: {self.name} user ID: {self.user_id}"

    def __eq__(self, user):
        """
        Compares two User objects for equality based on their attributes.

        Args:
        - other (User): other User object to compare.

        Returns:
        - bool: True if the users are same else False.
        """
        if isinstance(user, User):
            return (self.name == user.name and
                    self.user_id == user.user_id)
        return False

class Users:
    
    """
    Represents a collection of User objects.
    """

    def __init__(self, table: list=[]):
        """
        Initializes a Users object with an empty list to store users.

        Args:
        - table (list): list of dictionaries representing user data (default an empty list).
        """
        self.users = []
        self.headers = {'name', 'user_id'}
        
        # populate users from the table
        if table:
            for row in table[1:]:
                row_dict = {header: row[i] for i, header in enumerate(self.headers)}
                self.users.append(User(row_dict['name'], row_dict['user_id']))

    def search_by_name(self, name: str) -> list:
        """
        Searches for users in the collection by name

        Args:
        - name (str): name of the user to search for

        Returns:
        - list: list of dictionaries containing details of users matches with the name.
        """

        return [vars(user) for user in self.users if user.name == name]

    def search_by_id(self, user_id: int) -> list:
        """
        Searches for users in the collection by user ID.

        Args:
        - user_id (str): The ID of the user to search for.

        Returns:
        - list: list of dictionary containing details of the user matches with the ID.
        """
        return [vars(user) for user in self.users if user.user_id == user_id]

    def add_user(self, name: str, user_id: int) -> None:
        """
        Adds a new user to the collection

        Args:
        - name (str): name of the user to add.
        - user_id (str): The ID of the user to add.

        Returns:
        - None
        """
        exist_user = self.search_by_id(user_id)
        if len(exist_user) > 0:
            print(f"user already exists with the {user_id}")
            return
        user = User(name, user_id)
        self.users.append(user)

    def update_user(self, user_id: int, new_name: str = None) -> dict:
        """
        Updates the details (only name for now) of a user in the collection.

        Args:
        - user_id (str): The ID of the user to update.
        - new_name (str): new name for the user (default is None).

        Returns:
        - dict: A dictionary indicating the status of the update and the updated user details.
        """
        is_updated = False
        for user in self.users:
            if user.user_id == user_id:
                if new_name:
                    user.name = new_name
                is_updated = True
        return {"status": is_updated, "New details": vars(user)}

    def delete_user(self, user_id: int) -> dict:
        """
        Deletes a user from the collection.

        Args:
        - user_id (str): The ID of the user to delete.

        Returns:
        - bool: True if the user is deleted successfully, else False.
        """
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                return True
        return False  # User not found

    def list_users(self) -> None:
        """
        Prints the details of all users in the collection.
        """
        for user in self.users:
            print(user)