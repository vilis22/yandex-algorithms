class ManagedAttribute:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name, None)

    def __set__(self, instance, value):
        setattr(instance, self.private_name, value)


class User:
    name = ManagedAttribute()
    age = ManagedAttribute()


u1 = User()
u1.age = 20
print(u1.age)
print(u1.__dict__)  # Посмотрим, что внутри объекта
