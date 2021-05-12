'''def make_album(name,cd,number = None):
    singer_cd = {"name" : name,"cd" : cd,"number":number}
    return singer_cd
a = make_album("bbb","cccc",15)
print(a)'''
def make_album(name,cd,number = None):
    singer_cd = {"name" : name,"cd" : cd}
    if number:
        singer_cd['number'] = number
    return singer_cd
a = make_album("bbb","cccc")
print(a)