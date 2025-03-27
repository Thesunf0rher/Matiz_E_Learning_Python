from user import User

class Admin(User):
    """Статус админа в программе"""
    def __init__(self, first_name, last_name, age: int, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()

class Privileges:
    """Привилегии"""
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = ["разрешено добавлять сообщения",
                          "разрешено удалять пользователей",
                          "разрешено банить пользователей"]
            self.privileges = privileges

    def show_privileges(self):
        "Показывает привилегии администратор"
        for privilege in self.privileges:
            print(f"- {privilege}")
        print()
