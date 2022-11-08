# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from data_analice import parse_file, group_by_n, parse_file_des
from graphics import graphic_bar, graphic_bar_des, plot
import pandas as pd
from os import getcwd
from files import write


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = getcwd() + '/output/output_des/table_data.xlsx'
    values = group_by_n()
    csv = {
        'Count': [i for i in range(8, 19)]
    }
    for i in range(18, 32, 1):
        csv[f'N-{i}'] = []

    for value in values:
        for i, v in enumerate(value.values):
            if value.n >= 18:
                csv[f'N-{value.n}'].append(v.time)
        # while len(csv[f'N-{value.n}']) < 11:
        #     csv[f'N-{value.n}'].append(-1)
        plot(value)
        graphic_bar(value)
    df = pd.DataFrame(csv)
    latex = df.to_latex()
    print(latex)
    df.to_excel(path)
    csv = {
        'NumberBox': [],
        'Time': [],
        'K-1': [],
        'K-2': [],
        'K-3': [],
        'K-4': []

    }
    values = parse_file_des()
    for i, value in enumerate(values):
        csv['NumberBox'].append(i + 1)
        csv['Time'].append(value.time)
        for j, v in enumerate(value.values):
            csv[f'K-{j + 1}'].append(float(v))

        graphic_bar_des(value, i)
    df = pd.DataFrame(csv)
    latex = df.to_latex()
    path = getcwd() + '/output/output_des/table_des.txt'
    write(path, latex)
    print(df)
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
