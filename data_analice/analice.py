from files import read, read_directory
from os import getcwd


class DataOutput:
    def __init__(self, line: str, values=[]):
        line_split = line.split(" ")
        self.n = int(line_split[2])
        self.k = int(line_split[5])
        self.count = int(line_split[8])
        self.time = float(line_split[10].split('\n')[0])
        self.values = values


class DataGroupByN:
    def __init__(self, n, values: [DataOutput]):
        self.n = n
        self.k = values[0].k
        self.values = values


def parse_file():
    path = getcwd() + '/data/data.txt'
    data = read(path)
    values = list(map(lambda x: DataOutput(x), data))
    return values


def parse_file_des():
    path = getcwd() + '/data/data_des/'
    files_name = read_directory(path)
    files = list(map(lambda file: read(path + file), files_name))
    values = list(map(lambda x: DataOutput(x[0], x[1].split(' ')[:-1]), files))
    return values


def group_by_n():
    values = parse_file()
    group = {}
    for value in values:
        try:
            group[value.n].append(value)
        except:
            group[value.n] = [value]

    return list(map(lambda x: DataGroupByN(x, group[x]), group))
