import json
#favorite_number = input("\nwhat's your favorite number: ")
filename = "favorite_number.json"
with open(filename) as f:
    #ump(favorite_number,f)
    favorite_number = json.load(f)
print(f"I know your favorite number! It's {favorite_number}.")
