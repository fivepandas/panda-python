wudengke = {"first_name": "Wu",
            "Last_name" : "Dengke",
            "age" : 27,
            "city" : "Beijing"
            }
xiongyuejiao = {"first_name": "Xiong",
            "Last_name" : "Yuejiao",
            "age" : 26,
            "city" : "Beijing"
}
xiongjiujiu = {"first_name": "Xiong",
            "Last_name" : "jiujiu",
            "age" : 0.7,
            "city" : "Chongqing"
}
people = [wudengke,xiongyuejiao,xiongjiujiu]

for user_name in people:

    print(user_name)
    for key,value in user_name.items():
        print(f"{key}\n{value}")