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


user1 = User('raim', 'kad', 19, 'kazakhstan')
user2 = User('nur','auel', 19, 'kazakhstan')
user3 = User('dana','erm', 19, 'kazakhstan')

user1.describe_user()
user2.describe_user()
user3.describe_user()

user1.greet_user()