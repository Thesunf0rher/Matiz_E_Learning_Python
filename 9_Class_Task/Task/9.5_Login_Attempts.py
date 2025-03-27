class User:
    def __init__(self, first_name: str, last_name: str, age: int, location: str):
        """Информация о пользователе"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.location = location.title()
        self.login_attempts = 0

    def increment_login_attempts(self):
        """Добавляет +1 к количеству попыток входа"""
        self.login_attempts += 1
        print(f"Попыток входа: {self.login_attempts}")

    def reset_login_attempts(self):
        """Сбрасывает количество попыток входа"""
        self.login_attempts = 0
        print("Количество попыток входа сброшено.")

    def describe_user(self):
        """Выводит информацию о пользователе"""
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}\n")

    def greet_user(self):
        """Приветсвтие пользователя"""
        print(f"Hello, {self.first_name} {self.last_name}!")


user1 = User('raim', 'kad', 19, 'kazakhstan')


user1.describe_user()
user1.greet_user()

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
