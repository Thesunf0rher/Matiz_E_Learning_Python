
while True:
    age_input = input("Введите возраст (или 'quit' для выхода): ")

    if age_input.lower() == 'quit':
        break

    age = int(age_input)

    if age < 3:
        price = 'free'
    elif 3 <= age < 12:
        price = 10
    else:
        price = 15

    print(f"Цена билета: {price}$")