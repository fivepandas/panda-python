message = "How old are you?"
message += "\nEnter 'quit' to end the program. "

#age = input(message)

'''while age != 'quit':
    if int(age) < 3:
        print("Free")
    elif int(age) <= 12:
        print("$10")
    else:
        print("$15")
    age = input(message)'''
active = True
while active:
    age = input(message)
    if age == 'quit':
        active = False
    else:
        if int(age) < 3:
            print("Free")
        elif int(age) <= 12:
            print("$10")
        else:
            print("$15")


