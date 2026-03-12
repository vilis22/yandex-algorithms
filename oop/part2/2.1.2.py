class User:
    def __init__(self, username: str, email: str) -> None:
        self.username = username
        self.email = email

    @classmethod
    def from_string(cls, user_data_string: str) -> "User":
        username, email = user_data_string.split(",")
        return cls(username, email)
