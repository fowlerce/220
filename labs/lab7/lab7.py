"""
Name: Christian Fowler
lab7.py

Problem: Bumper cars simulation

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""

from graphics import *

from random import randint

import math

## ---------------------------- ## Helper Functions ## ---------------------------- ##

def get_random(move_amt):
    return randint(-move_amt, move_amt)

def get_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return color_rgb(red, green, blue)

def did_collide(circle1, circle2):
    circ1_center = circle1.getCenter()
    circ2_center = circle2.getCenter()
    dist = math.sqrt(((circ2_center.getX() - circ1_center.getX())**2) + ((circ2_center.getY() - circ1_center.getY())**2))
    if (circle1.getRadius() + circle2.getRadius()) <= dist:
        return False
    else:
        return True

def hit_vertical(circle, Graphwin):
    top_edge = circle.getCenter().getY() - int(circle.getRadius())
    bottom_edge = circle.getCenter().getY() + int(circle.getRadius())
    if top_edge <= 0:
        return True
    if bottom_edge >= Graphwin.getHeight():
        return True
    else:
        return False

def hit_horizontal(circle, Graphwin):
    left_edge = circle.getCenter().getX() - int(circle.getRadius())
    right_edge = circle.getCenter().getX() + int(circle.getRadius())
    if left_edge <= 0:
        return True
    if right_edge >= Graphwin.getWidth():
        return True
    else:
        return False

## ---------------------------- ## Main Function ## ---------------------------- ##

def bumper():
    width = 750
    height = 750
    win = GraphWin("Bumper Cars", width, height)

# Creates circles
    # Generates circles' random start points w/ get_random()
    circ1_x = randint(100, 650)
    circ1_y = randint(100, 650)
    circ2_x = randint(100, 650)
    circ2_y = randint(100, 650)

    circ1_start = Point(circ1_x, circ1_y)
    circ2_start = Point(circ2_x, circ2_y)

    circ1 = Circle(circ1_start, 100)
    circ2 = Circle(circ2_start, 100)

    # Generates circles' random color w/ get_random_color()

    circ1.setFill(get_random_color())
    circ1.draw(win)
    circ2.setFill(get_random_color())
    circ2.draw(win)

    win.getMouse()

# Moves circles
    # Generates circles' random move values
    circ1_x_direct = get_random(15)
    circ1_y_direct = get_random(15)
    circ2_x_direct = get_random(15)
    circ2_y_direct = get_random(15)

    while not win.checkMouse():
        circ1.move(circ1_x_direct, circ1_y_direct)
        circ2.move(circ2_x_direct, circ2_y_direct)
        time.sleep(0.1)
        if did_collide(circ1, circ2):
            circ1_x_direct = circ1_x_direct * -1
            circ1_y_direct = circ1_y_direct * -1
            circ2_x_direct = circ2_x_direct * -1
            circ2_y_direct = circ2_y_direct * -1
        if hit_vertical(circ1, win):
            circ1_y_direct = circ1_y_direct * -1
        if hit_vertical(circ2, win):
            circ2_y_direct = circ2_y_direct * -1
        if hit_horizontal(circ1, win):
            circ1_x_direct = circ1_x_direct * -1
        if hit_horizontal(circ2, win):
            circ2_x_direct = circ2_x_direct * -1

# Close
    close = Text(Point((win.getWidth() / 2), (win.getHeight() / 2)), 'Click Anywhere to Close Window')
    close.setSize(25)
    close.setFill('white')
    close.draw(win)
    win.getMouse()
    win.close()

# Runs program
get_random(15)
get_random_color()
bumper()
