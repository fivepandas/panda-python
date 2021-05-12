from name_function import get_formmted_name
print("Enter 'q' at any time to quit")
while True:
    first = input("\n Please give me a first name:")
    if first =='q':
        break
    last = input("please give me a last name:")
    if last == 'q':
        break
    fomatted_name = get_formmted_name(first,last)
    print(f"\tNeatly formatted name:{fomatted_name}")