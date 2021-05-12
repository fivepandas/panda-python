def file(filename):
    try:
        with open(filename) as f:

            contents = f.read()
            print(contents)
    except FileNotFoundError:
           pass
file('cat.txt')