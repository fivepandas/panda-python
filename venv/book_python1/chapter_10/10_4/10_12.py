import json
filename = 'favorite_number.json'
try:
    with open(filename) as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    favorite_number = input("what's your favorite number")
    json.dump(favorite_number,f)
else:
    print(f"your favorite number is {favorite_number}.")

