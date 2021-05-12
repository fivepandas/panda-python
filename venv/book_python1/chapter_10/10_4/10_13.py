import json
def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f:
           username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    """提示用户输入用户名。"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username
def greet_user():
    username = get_stored_username()
    if username:
        jud = input(f"Is {username} your name ?'Y' OR 'N'")
        if jud == "Y":
            print(f"Welcome back,{username}")
        else:
            username = get_new_username()
    else:
        username =  get_new_username()

        print(f"We'll remember you when you conme back,{username}")

greet_user()
