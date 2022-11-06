# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from data_analice import parse_file, group_by_n
from graphics import graphic_bar


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    values = group_by_n()
    for value in values:
        graphic_bar(value)

    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
