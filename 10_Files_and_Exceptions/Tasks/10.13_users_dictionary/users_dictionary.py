from pathlib import Path
import json

def get_stored_username(path):
    """Получаем хранимое имя пользователя, если оно существует."""
    if path.exists():
        contents = path.read_text(encoding='utf-8')
        return json.loads(contents)
    else:
        return None

def get_new_user(path):
    """Запрашиваем новое имя пользователя"""
    user_info = {
        'Username': input("What is your username? "),
        'First_name': input("What is your first name? "),
        'Last_name': input("What is your last name? "),
    }

    path.write_text(json.dumps(user_info, ensure_ascii=False), encoding="utf-8")
    return user_info

def greet_user():
    """Приветствует пользователя по имени."""
    path = Path('username.json')

    user_data = get_stored_username(path)

    if user_data:
        print(f"Welcome back, {user_data['Username']}, {user_data['First_name']}, {user_data['Last_name']}!")
    else:
        user_data = get_new_user(path)
        print(f"We'll remember you when you come back, {user_data['Username']}, {user_data['First_name']} {user_data['Last_name']}!")

greet_user()