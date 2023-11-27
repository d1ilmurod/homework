class Users:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def greet(self):
        print(f"Hello {self.name} {self.last_name}")


class Admin(Users):
    def ban_user(self, user):
        print(f"Foydalanuvchi bloklandi {self.name} {self.last_name}")


user1 = Users('Ali', 'Valiyev')
admin1 = Admin('Hasan', 'Husanov')

user1.greet()

admin1.greet()


admin1.ban_user(user1)


