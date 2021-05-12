class User:
    def __init__(self,first_name,last_name):
        self.first = first_name
        self.last = last_name
        self.login_attempts = 0
    def describe_user(self):
        print(f"\nthe user's first name is {self.first},the user's last name is {self.last}")
    def greet_user(self):
        print(f"Hello,{self.first} {self.last}")
    def increment_login_attempts(self):
        self.login_attempts +=1
    def reset_login_attempts(self):
        self.login_attempts = 0
user_1 = User('yuejiao',"xiong")
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(user_1.login_attempts)
user_1.reset_login_attempts()
print(user_1.login_attempts)
