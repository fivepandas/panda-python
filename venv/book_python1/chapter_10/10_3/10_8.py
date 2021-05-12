def file(filename):
    try:
        with open(filename) as f:

            contents = f.read()
            print(contents)
    except FileNotFoundError:
            print("the file does not exist.")
file('cat.txt')