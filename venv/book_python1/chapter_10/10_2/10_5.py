filename = 'reason.txt'
with open(filename,'a') as f:
    while True:
        reason = input("why you love programming: ")
        if reason == 'q':
            break
        else:
            f.write(f"{reason}\n")
