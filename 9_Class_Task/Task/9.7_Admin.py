class User:
    def __init__(self, first_name: str, last_name: str, age: int, location: str):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.location = location.title()

    def describe_user(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}\n")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")

class Admin(User):
    """Статус админа в программе"""
    def __init__(self, first_name, last_name, age: int, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = ["разрешено добавлять сообщения",
                           "разрешено удалять пользователей",
                           "разрешено банить пользователей"]

    def show_privileges(self):
        "Показывает привилегии администратор"
        print(f"Привилегии администратора {self.first_name} {self.last_name}:")
        for privilege in self.privileges:
            print(f"- {privilege}")
        print()



admin1 = Admin('raim','kad', 19, 'KZ')

admin1.show_privileges()

#210