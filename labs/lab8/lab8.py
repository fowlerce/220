"""
Name: Christian Fowler
lab8.py

Problem: Uses numeric data from a text file to calculate weighted averages

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""

def weighted_average(in_file_par, out_file_par):
    in_file = open(in_file_par, 'r')
    out_file = open(out_file_par, 'w')
    in_file_lines = in_file.readlines()
    class_grades_sum = 0
    student_counter = 0
    for line in in_file_lines:
        line_splitter = line.split(':')
        names = line_splitter[0]
        grades_and_weights = line_splitter[1]
        grades = grades_and_weights.strip().split(' ')
        sum = 0
        check_if_100 = 0
        for x in range(0, len(grades), 2):
            check_if_100 = check_if_100 + eval(grades[x])
        if (check_if_100 == 100):
            student_counter = student_counter + 1
            for y in range(0, len(grades), 2):
                product = eval(grades[y]) * eval(grades[y + 1])
                sum = sum + product
            wtd_avg = sum / 100
            class_grades_sum = class_grades_sum + wtd_avg
            output = '{:<1}'.format(wtd_avg)
            out_file.write('{}\'s average: {} \n'.format(names, wtd_avg))
        elif (check_if_100 > 100):
            wtd_avg = 'Error: The weights are more than 100'
            output = '{}\'s average: {} \n'.format(names, wtd_avg)
            out_file.write(output)
        elif (check_if_100 < 100):
            wtd_avg = 'Error: The weights are less than 100'
            output = '{}\'s average: {} \n'.format(names, wtd_avg)
            out_file.write(output)
    class_avg = class_grades_sum / student_counter
    out_file.write('{} {}'.format('Class average:', str(class_avg)))
    in_file.close()
    out_file.close()

if __name__ == '__main__':
    weighted_average("grades.txt", "avg.txt")
