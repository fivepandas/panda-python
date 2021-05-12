from Admin import Admin
user = Admin('Yuejiao', 'Xiong')
user.describe_user()
user_privileges = ['can add post','can delete post','can ban user']
user.privileges.privileges = ['can add post','can delete post','can ban user']
user.privileges.show_privileges()