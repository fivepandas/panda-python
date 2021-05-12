class User:
    def __init__(self,first_name,last_name):
        self.first = first_name
        self.last = last_name
    def describe_user(self):
        print(f"\nthe user's first name is {self.first},the user's last name is {self.last}")
    def greet_user(self):
        print(f"Helle,{self.first} {self.last}")
user_1 = User('Yuejiao','Xiong')
user_2 = User('dengke',"Wu")
user_3 = User("Zhuzhu",'Wu')
user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()
user_3.describe_user()
user_3.greet_user()

