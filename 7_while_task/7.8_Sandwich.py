sandwich_orders = ['club sandwich', 'cuban sandwich', 'ruben','filly cheesesteak', 'ban  mi',]
finished_sandwiches = []
# Сделал через цикл for
# for sandwich in sandwich_orders:
#     finished_sandwiches.append(sandwich)
#     print(f"I have prepared {sandwich.title()}")


while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"The sandwich is ready: {sandwich}")
    finished_sandwiches.append(sandwich)

for sandwiches in finished_sandwiches:
    print(sandwiches.title())