print('give me two numbers I will plus them.')
print("enter q to quit")
while True:
    first_number = input('please give me the first number:')
    if first_number == "q":
        break
    second_number = input('Please give me the second number:')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        pass
    else:
        print(answer)