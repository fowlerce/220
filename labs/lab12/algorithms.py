"""
Name: Christian Fowler
algorithms.py

Problem: Reads a .txt file and provides a linear search function

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""


def read_data(filename):
    in_file = open(filename, 'r')
    lines_list = in_file.readlines()
    main_counter = 0
    word_counter = 0
    output = []
    while main_counter <= len(lines_list) - 1:
        line = lines_list[main_counter]
        while word_counter <= len(line) - 1:
            output.append(line[word_counter])
            word_counter = word_counter + 1
        word_counter = 0
        main_counter = main_counter + 1
    return output


def is_in_linear(search_val, values):
    counter = 0
    found = False
    while counter <= len(values) - 1 and not found:
        if values[counter] == search_val:
            found = True
        else:
            counter = counter + 1
    return found

