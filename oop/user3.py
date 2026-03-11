class User:
    def __init__(self, username):
        self.username = username


class Admin(User):
    def __init__(self, username, access_level):
        super().__init__(username)
        self.access_level = access_level


def get_user_description(user_object):
    if isinstance(user_object, Admin):
        return f"Администратор {user_object.username} с уровнем доступа {user_object.access_level}"
    elif isinstance(user_object, User):
        return f"Пользователь {user_object.username}"
