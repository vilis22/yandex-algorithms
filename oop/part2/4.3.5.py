class LoggedAccess:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        print(f"Чтение атрибута '{self.public_name}'")
        return getattr(instance, self.private_name, None)

    def __set__(self, instance, value):
        print(f"Запись атрибута '{self.public_name}', новое значение = {value}")
        setattr(instance, self.private_name, value)
