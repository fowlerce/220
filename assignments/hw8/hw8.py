"""
Name: Christian Fowler
hw8.py

Problem: Working with conditionals

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""

import math
from graphics import *

def add_ten(nums_par):
    for i in range(len(nums_par)):
        nums_par[i] = nums_par[i] + 10

def square_each(nums_par):
    for i in range(len(nums_par)):
        nums_par[i] = nums_par[i] ** 2

def sum_list(nums_par):
    sum = 0
    for i in range(len(nums_par)):
        sum = sum + nums_par[i]
    return sum

def to_numbers(nums_par):
    for i in range(len(nums_par)):
        nums_par[i] = float(nums_par[i])

def sum_of_squares(par):
    new_list = []
    for i in range(len(par)):
        sum = 0
        my_string = ''
        splitter = str(par[i]).split(',')
        for j in range(len(splitter)):
            stripper = str(splitter[j]).strip()
            squares = float(stripper) ** 2
            sum = sum + squares
            my_string = my_string + stripper
        new_list.append(sum)
    return new_list

def starter(weight_par, wins_par):
    if weight_par >= 150 and weight_par < 160 and int(wins_par) >= 5:
        Starter = True
    elif weight_par > 199 or int(wins_par) > 20:
        Starter = True
    else:
        Starter = False
    return Starter

def leap_year(year_par):
    # This problem was worded terribly.
    # After this, I'm questioning if I even understand what a leap year is.
    if int(year_par) % 4 == 0 or int(year_par) % 400 == 0 and int(year_par) % 100 != 0:
        leap = True
    else:
        leap = False
    return leap

def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    circle_overlap.center_1 = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (circle_overlap.center_1.getX() - circumference_point.getX()) ** 2 + (circle_overlap.center_1.getY() - circumference_point.getY()) ** 2)
    circle_overlap.circle_one = Circle(circle_overlap.center_1, radius)
    circle_overlap.circle_one.setFill("light blue")
    circle_overlap.circle_one.draw(win)

    circle_overlap.center_2 = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt((circle_overlap.center_2.getX() - circumference_point.getX()) ** 2 + (circle_overlap.center_2.getY() - circumference_point.getY()) ** 2)
    circle_overlap.circle_two = Circle(circle_overlap.center_2, radius)
    circle_overlap.circle_two.setFill("light blue")
    circle_overlap.circle_two.draw(win)

    win.getMouse()

def did_overlap(circle_one, circle_two):
    circle_overlap.circle_one = circle_one
    circle_overlap.circle_two = circle_two
    dist = math.sqrt(((circle_overlap.center_2.getX() - circle_overlap.center_1.getX()) ** 2) + ((circle_overlap.center_2.getY() - circle_overlap.center_1.getY()) ** 2))
    if (circle_one.getRadius() + circle_two.getRadius()) <= dist:
        return False
    else:
        return True

if __name__ == '__main__':
    pass
