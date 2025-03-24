def greet_users(names):
    """Выводит простое приветствие для каждого пользователя в списке."""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)

username = ['hannah', 'ty', 'marget']
greet_users(username)
