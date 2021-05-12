guests_name = input('please input your name: ')
filename = 'guest'
with open(filename,'a') as file_object:
    file_object.write(guests_name)