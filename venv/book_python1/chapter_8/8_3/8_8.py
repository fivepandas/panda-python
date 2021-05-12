def make_album(name,cd,number = None):
    singer_cd = {"name" : name,"cd" : cd}
    if number:
        singer_cd['number'] = number
    return singer_cd

while True:
    print("enter 'q' to quit at any time")
    name = input("\nThe singer's name is:")
    if name == 'q':
        break
    cd = input("the cd is :")
    if cd == 'q':
        break
    a = make_album(name,cd)


    print(a)