users = ['jon','admin','lisa','leo','miki']

for user in users:
    if user == 'admin':
        print(f"Здравствуйте, admin, хотите просмотреть отчет о состоянии дел?")
    else:
        print(f"Привет, {user}, спасибо, что авторизовался в системе")