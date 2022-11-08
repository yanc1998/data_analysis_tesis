from os import getcwd, listdir


def read(path: str):
    with open(path) as f:
        lines = f.readlines()

    return lines


def write(path, data):
    print(data)
    with open(path) as f:
        f.write(data)


def read_directory(path: str):
    list_dirs = listdir(path)
    return list(filter(lambda file: file.endswith('.txt'), list_dirs))


def testRead():
    cwd = getcwd()
    path = cwd + '/data/data.txt'
    a = read(path)
    print(a)
