print('give me two numbers I will plus them.')
print("enter q to quit")
while True:
    try:
        first_number = int(input('please give me the first number:'))
        if first_number == "q":
            break
        second_number = int(input('Please give me the second number:'))
        if second_number == 'q':
            break
        answer = first_number + second_number


    except ValueError:
       print("wrong")
    else:
        print(answer)