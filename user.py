#Manage users (add, update, delete, list, and search by attributes like name, user ID

class User:
    def __init__(self, name: str, user_id: str):
        self.name = name
        self.user_id = user_id
    
    def __str__(self) -> str:
        return f"Name: {self.name} user ID: {self.user_id}"

    def __eq__(self, user):
        if isinstance(user, User):
            return (self.name == user.name and
                    self.user_id == user.user_id)
        return False

class Users:
    def __init__(self, table: list=[]):
        self.users = []
        self.headers = {'name', 'user_id'}
        
        # populate users from the table
        if table:
            for row in table[1:]:
                row_dict = {header: row[i] for i, header in enumerate(self.headers)}
                self.users.append(User(row_dict['name'], row_dict['user_id']))

    def search_by_name(self, name: str) -> list:
        return [vars(user) for user in self.users if user.name == name]

    def search_by_id(self, user_id: int) -> list:
        return [vars(user) for user in self.users if user.user_id == user_id]

    def add_user(self, name: str, user_id: int) -> None:
        exist_user = self.search_by_id(user_id)
        if len(exist_user) > 0:
            print(f"user already exists with the {user_id}")
            return
        user = User(name, user_id)
        self.users.append(user)

    def update_user(self, user_id: int, new_name: str = None) -> dict:
        is_updated = False
        for user in self.users:
            if user.user_id == user_id:
                if new_name:
                    user.name = new_name
                is_updated = True
        return {"status": is_updated, "New details": vars(user)}

    def delete_user(self, user_id: int) -> dict:
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                return True
        return False  # User not found

    def list_users(self) -> None:
        for user in self.users:
            print(user)