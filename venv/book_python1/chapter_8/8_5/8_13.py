def build_profile(first,last,**user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('Yuejiao','Xiong',
                             location = 'Beijing',
                             husband = 'wudengke',
                             intrist = 'cooking')
print(user_profile)