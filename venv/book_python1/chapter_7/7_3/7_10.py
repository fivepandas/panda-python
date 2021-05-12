places = {}
go = True
while go:
    name = input("what's your name?")
    place = input("If you could visit one place in the world, where would you go?")
    places[name] = place
    repeat = input("If you could visit one place in the world, where would you go?")
    if repeat == "no":
        go = False
for name , place in places.items():
    print(f"{name} would like to go {place}.")