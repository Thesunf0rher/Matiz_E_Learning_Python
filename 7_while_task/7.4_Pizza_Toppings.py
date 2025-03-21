prompt = "\nНапишите какую начинку добавить в ваш заказ: "
prompt += "\nЕсли вы закончили с начинкой, напишите 'quit'"

toppings = []

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        toppings.append(topping.title())
        print(f"В вашем пицце такие начинки: {', '.join(toppings)}")