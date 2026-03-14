class DictMixin:
    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self._password_hash = None


class SerializableUser(DictMixin, User):
    pass


if __name__ == "__main__":
    user = SerializableUser("Ivan", "ivan@mail.com")
    print(user.to_dict())
