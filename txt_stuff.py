def dictionary():
    files = []
    with open('recepies.txt', 'rt') as file:
        counting = file.readline()
    files.append(counting)
    print(files)
dictionary()
