user_database = []
""" 
 - The above simulates a database
 - The self argument determines object data
 - The static method does note require object
    instances
 -      
"""


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    @staticmethod
    def get_user(user_id):
        for user in user_database:
            if int(user.id) == int(user_id):
                return

    @staticmethod
    def get_users():
        return user_database

    def store_user(self):
        user_id = len(user_database) + 1
        self.id = user_id
        user_database.append(self)
        return True