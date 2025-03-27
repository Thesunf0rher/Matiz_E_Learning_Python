from random import choice, randint

number_list = [5,3,7,9,1,2,3,1,8,5,'a','s','d','f','g']

# chatGPT
# player1 = [choice(number_list) for _ in range(4)]
# finish = [choice(number_list) for _ in range(4)]
#
# print("Билет игрока:", ", ".join(map(str,player1)))
# print("Выигрышный билет:", ", ".join(map(str, finish)))

#my
player1 = f"{choice(number_list)} {choice(number_list)} {choice(number_list)} {choice(number_list)}"
finish = f"{choice(number_list)} {choice(number_list)} {choice(number_list)} {choice(number_list)}"

print(player1)
print(finish)
