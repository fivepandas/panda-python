filename = 'guest.txt'
with open(filename, 'a') as file_object:
    while True:
        guests_name = input('please input your name: ')
        if guests_name == 'q':
            break
        else:

            file_object.write(f"{guests_name}\n")
            file_object.flush()
            print(f"Hello,{guests_name}!")
