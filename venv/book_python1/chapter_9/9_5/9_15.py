from random import choice
my_ticket = []
cycle = 0
while my_ticket != ['d', 8, 4, 'c']:
    cycle += 1
    count = 0
    lottery = ['a', 'b', 'c', 'd', 'k', 1, 2, 3, 4, 6, 90, 7, 8, 9, 80]
    while count < 4:
        count += 1
        lottery_1 = choice(lottery)
        lottery.remove(lottery_1)
        my_ticket.append(lottery_1)

print(cycle)