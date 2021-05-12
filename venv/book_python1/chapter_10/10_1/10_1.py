filename = 'learnin_python.txt'
with open(filename) as file_object:
    'contents = file_object.read()'
    '''for lne in file_object:
        print(lne.rstrip())'''
    lines = file_object.readlines()
for line in lines:
    print(line)