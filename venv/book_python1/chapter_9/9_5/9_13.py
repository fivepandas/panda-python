class Die:
    def __init__(self, sides=6):
        self.sides = sides
    def roll_die(self):
        from random import randint
        a = randint(1, self.sides)
        print(f"you got  {a}")
'''a_6 = Die()
count = 0
while count < 10:
    count += 1
    a_6.roll_die()'''
'''a_10 = Die(10)
count = 0
while count < 10:
    count += 1
    a_10.roll_die()'''


