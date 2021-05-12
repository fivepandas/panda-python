from random import choice
lottery = ['a', 'b', 'c', 'd', 'k', 1, 2, 3, 4, 6, 90, 7, 8, 9, 80]

count = 0
new_lotterys = []
while count < 4:
    count += 1
    lottery_1 = choice(lottery)
    lottery.remove(lottery_1)
    new_lotterys.append(lottery_1)
print(new_lotterys)
print("If you got the four numbers or letters,you got the lottery.")
