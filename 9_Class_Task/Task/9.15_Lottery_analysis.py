from random import choice, randint

number_list = [5,3,7,9,1,2,3,1,8,5,'a','s','d','f','g']

finish = [choice(number_list) for _ in range(4)]

cycle = 0

while True:

    player1 = [choice(number_list) for _ in range(4)]
    cycle += 1

    if player1 == finish:
        print("Вы выиграли")
        print(cycle)
        break
