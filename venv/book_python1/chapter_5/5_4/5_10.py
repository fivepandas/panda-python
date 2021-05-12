current_users = ['admin','david','lily','alan','keke','ross']
new_users = ['Alan','richal','Ross','amy','emily']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("please choose another user name.")
    else:
        print("this user haven't been used yet.")