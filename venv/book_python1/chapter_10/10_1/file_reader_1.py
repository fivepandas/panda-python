filename = 'pi_digits.txt'
with open(filename) as file_object:
    '''for line in file_object:
        print(line)'''
    lines = file_object.readlines()
'''for line in lines:
    print(line.rstrip())'''
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))