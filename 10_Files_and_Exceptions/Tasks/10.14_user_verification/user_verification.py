from pathlib import Path
import json

def get_stored_username(path):
    """Получаем хранимое имя пользователя, если оно существует."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """Запрашиваем новое имя пользователя"""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Приветствует пользователя по имени."""
    path = Path('username.json')
    username = get_stored_username(path)

    if username:
        correct_name = input(f"Is your name {username}? (yes/no)").lower()
        if correct_name != "yes":
            username = get_new_username()
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()
