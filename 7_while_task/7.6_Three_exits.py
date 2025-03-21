#7.5 улучшенная версия
# active = True
#
# while active:
#     age_input = input("Введите возраст (или 'quit' для выхода): ")
#
#     if age_input.lower() == 'quit':
#         break
#
#     age = int(age_input)
#
#     if age < 3:
#         price = 'free'
#     elif 3 <= age < 12:
#         price = 10
#     else:
#         price = 15
#
#     print(f"Цена билета: {price}$")
#
#     if price == 'free':
#         active = False


# 7.4 улучшенная версия
# prompt = "\nНапишите какую начинку добавить в ваш заказ: "
# prompt += "\nЕсли вы закончили с начинкой, напишите 'quit'"
#
# toppings = []
#
# active = True
#
# while active:
#     topping = input(prompt)
#
#     if topping == 'quit':
#         break
#     else:
#         toppings.append(topping.title())
#         print(f"В вашем пицце такие начинки: {', '.join(toppings)}")
#
#     #Тут добавили ограничение максимум 5
#     if len(toppings) == 5:
#         active = False