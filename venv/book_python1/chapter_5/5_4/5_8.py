names = ['admin','david','lily','alan','keke','ross']
del names[0:6]
if names:
    for name in names:
        if name == 'admin':
            print(f"Hello {name},would you like to see a status report?")
        else:
            print(f'Hello {name},thank you for logging in again.')
else:
    print('We need find some users.')
