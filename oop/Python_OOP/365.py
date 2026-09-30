class User:
    def __init__(self, name, psw):
        self.name = name
        self.psw = psw

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Имя должно быть типом str")

        self._name = value

    @property
    def psw(self):
        return self._psw

    @psw.setter
    def psw(self, value):
        if not isinstance(value, str):
            raise TypeError("Пароль должен быть типом str")

        if not (set("!@#$&") & set(value)):
            raise TypeError('Нет ни одного из символов - "!@#$&"')

        if not any(char.isupper() for char in value):
            raise TypeError("Нет заглавных букв")

        if not any(char.islower() for char in value):
            raise TypeError("Нет строчных букв")

        self._psw = hash(value)

    def __repr__(self):
        return self.name


class DB:
    def __init__(self, *users):
        names = [user.name for user in users]

        if len(names) != len(set(names)):
            raise TypeError("Добавлены пользователи с одинаковыми никнеймами!")

        self._db = []

        for i, user in enumerate(users, start=1):
            self._db.append((i, user))

    def __setattr__(self, key, value):
        if key == "_db" and "_db" in self.__dict__:
            raise TypeError("Низзяяя!!!")

        object.__setattr__(self, key, value)

    def add_user(self, *users):
        existing = {user.name for _, user in self._db}

        for user in users:
            if user.name in existing:
                raise TypeError("Пользователь с таким именем уже есть в базе!")

            existing.add(user.name)

        for user in users:
            next_id = len(self._db) + 1
            self._db.append((next_id, user))
