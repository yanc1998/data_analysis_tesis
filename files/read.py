from os import getcwd


def read(path: str):
    with open(path) as f:
        lines = f.readlines()

    return lines


def testRead():
    cwd = getcwd()
    path = cwd + '/data/data.txt'
    a = read(path)
    print(a)
