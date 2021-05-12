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
        self.privileges = [ ]
    def show_privileges(self):
        privileges = self.privileges
        print(f"\n{self.last} {self.first}'s privileges include:")
        for privilege in privileges:
            print(f"-{privilege}")
Admin_1 = Admin("Yuejiao","Xiong",)
Admin_1.privileges = ['can add post','can delete post','can ban user']
Admin_1.show_privileges()

