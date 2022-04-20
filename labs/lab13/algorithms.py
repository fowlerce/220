"""
Name: Christian Fowler
algorithms.py

Problem: Reads a .txt file and provides linear search and binary search function

Certification of Authenticity:
<include one of the following>
I certify that this assignment is mostly my own work.
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
    in_file.close()
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


# Reminder to self: This algorithm is meant for SORTED lists.
def is_in_binary(search_val, values):
    found = False
    low_point = 0
    high_point = len(values)
    while low_point <= high_point and not found:
        mid_point = (low_point + high_point)//2
        if values[mid_point] < search_val:
            low_point = mid_point + 1
        elif values[mid_point] > search_val:
            high_point = mid_point - 1
        elif values[mid_point] == search_val:
            found = True
            return found
    return found


def selection_sort(values):
    for i in range(len(values)):
        low = i
        for j in range(i + 1, len(values)):
            if values[low] > values[j]:
                low = j
        values[i], values[low] = values[low], values[i]


def calc_area(rect):
    point1 = rect.getP1()
    point2 = rect.getP2()
    length = abs(point1.getX() - point2.getX())
    width = abs(point1.getY() - point2.getY())
    area = length * width
    return area


def rect_sort(rectangles):
    areas_list = []
    for rect in rectangles:
        area = calc_area(rect)
        areas_list.append(area)
    selection_sort(areas_list)

