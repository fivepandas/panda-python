class User:
    def __init__(self,first_name,last_name):
        self.first = first_name
        self.last = last_name
    def describe_user(self):
        print(f"\nthe user's first name is {self.first},the user's last name is {self.last}")
    def greet_user(self):
        print(f"Helle,{self.first} {self.last}")
class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges = Privileges()
    '''def show_privileges(self):
        privileges = self.privileges
        print(f"\n{self.last} {self.first}'s privileges include:")
        for privilege in privileges:
            print(f"-{privilege}")'''
class Privileges:
    def __init__(self,privileges = []):
        self.privileges = privileges
    def show_privileges(self):
        for privilege in self.privileges:
            print(f"-{privilege}")
user_1 = Admin('yuejiao','xiong')
user_1.describe_user()
user_1.privileges.show_privileges()
user_1_privileges = ['can add post','can delete post','can ban user']
user_1.privileges.privileges = user_1_privileges
user_1.privileges.show_privileges()