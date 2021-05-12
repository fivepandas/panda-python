favorite_places = {'wudengke' : ['bed','lake','office'],
                   'xiongyuejiao' : ['bed','ocean','chengdu'],
                   'wuzhuzhu' : ['bed','home','outside']
                   }
for name, places in favorite_places.items():
    print(f"{name}'s favorite place is:\t")
    for place in places:
        print(f"\t{place}")
