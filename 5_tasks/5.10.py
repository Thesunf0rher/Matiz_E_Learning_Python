current_users = ['Jon','LInus','nick','lisa','jane']
new_users = ['jon','linus','den','dan','smit']

lower_users = [item.lower() for item in current_users]

for user in new_users:
    if user.lower() in lower_users :
        print(f"{user} Такой логин занят!")
    else:
        print(f"{user} Логин создан")
