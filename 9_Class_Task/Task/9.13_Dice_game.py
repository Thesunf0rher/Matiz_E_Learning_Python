from random import randint

class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        result = randint(1, self.sides)
        print(f"Вам выпало цифра: {result}")

cube1 = Die()
cube2 = Die(10)
cube3 = Die(20)

for i in range(10):
    print(f"Бросок номер: {i+1}")
    cube1.roll_die()
    cube2.roll_die()
    cube3.roll_die()
    print('-' * 30)
