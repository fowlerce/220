"""
Name: Christian Fowler
lab5.py

Problem: Continues practice with graphics, loops, and strings.

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""

from graphics import *

import math

def triangle():
    width = 500
    height = 500
    win = GraphWin("Triangle", width, height)

    instructions = Text(Point((win.getWidth() / 2), (win.getHeight() -20)), "Click 3 times to draw the corners of a triangle")
    instructions.setSize(15)
    instructions.setTextColor('red')
    instructions.draw(win)

    corner1 = win.getMouse()
    corner2 = win.getMouse()
    corner3 = win.getMouse()

    point1 = Point(corner1.getX(), corner1.getY())
    point2 = Point(corner2.getX(), corner2.getY())
    point3 = Point(corner3.getX(), corner3.getY())

    #distance between coordinates, for calculating length
    dx1 = abs(point1.getX() - point2.getX())
    dy1 = abs(point1.getY() - point2.getY())
    dx2 = abs(point2.getX() - point3.getX())
    dy2 = abs(point2.getY() - point3.getY())
    dx3 = abs(point3.getX() - point1.getX())
    dy3 = abs(point3.getY() - point3.getY())

    #length calculations
    a = math.sqrt((dx1**2) + (dy1**2))
    b = math.sqrt((dx2**2) + (dy2**2))
    c = math.sqrt((dx3**2) + (dy3**2))

    #perimeter calcualtion
    perimeter = a + b + c

    #area calculations using Herron's formula
    h = (a + b + c)/2
    area = math.sqrt(h * (h - a) * (h - b) * (h - c))

    triangle = Polygon(point1, point2, point3)
    triangle.setOutline('red')
    triangle.setFill('yellow')
    triangle.draw(win)

    #displays perimeter
    peri_message = Text(Point((win.getWidth() / 2), (win.getHeight() - 35)), 'Perimeter: {}'.format(perimeter))
    peri_message.setSize(15)
    peri_message.setFill('red')
    peri_message.draw(win)

    #displays area
    area_message = Text(Point((win.getWidth() / 2), (win.getHeight() - 50)), 'Area: {}'.format(area))
    area_message.setSize(15)
    area_message.setFill('red')
    area_message.draw(win)

    time.sleep(1)

    #closes window
    close = Text(Point((win.getWidth() / 2), (win.getHeight() - 65)), 'Click again to close')
    close.setSize(15)
    close.setTextColor('red')
    close.draw(win)

    win.getMouse()
    win.close()

def color_shape():
    width = 500
    height = 500
    win = GraphWin("Color Shape", width, height)

    instructions = Text(Point((win.getWidth() / 2), (win.getHeight() - 20)), "")
    instructions.setSize(15)
    instructions.setTextColor('red')
    instructions.draw(win)

def color_shape():
    #Creates window
    width = 500
    height = 500
    win = GraphWin("Color Shape", width, height)
    win.setBackground("white")

    #Creates text instructions
    msg = "Enter color values between 0 - 255"
    msg2 = "Click window to color shape"
    inst = Text(Point(width / 2, height - 30), msg)
    inst2 = Text(Point(width / 2, height - 10), msg2)
    inst.setSize(15)
    inst2.setSize(15)
    inst.setFill('red')
    inst2.setFill('red')
    inst.draw(win)
    inst2.draw(win)

    #Creates a circle in window's center
    shape = Circle(Point(width / 2, height / 2 - 30), 50)
    shape.draw(win)

    #redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(width / 2 - 50, height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    #green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    #blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    #Displays rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    #Displays Entry Labels
    red_entry = Entry(Point(width / 2 - 20, height / 2 + 40), 3)
    red_entry.draw(win)
    green_entry = Entry(Point(width / 2 - 20, height / 2 + 70), 3)
    green_entry.draw(win)
    blue_entry = Entry(Point(width / 2 - 20, height / 2 + 100), 3)
    blue_entry.draw(win)

    #Pauses for further user input
    msg3 = Text(Point(width / 2, height - 50), "Click again to input new colors")
    msg3.setSize(15)
    msg3.setFill('red')
    msg3.draw(win)

    #Changes shape color
    for i in range(5):
        win.getMouse()
        red = eval(red_entry.getText())
        green = eval(green_entry.getText())
        blue = eval(blue_entry.getText())
        shape.setFill(color_rgb(red, green, blue))

    #Displays "close window" instructions
    close = Text(Point((win.getWidth() / 2), (win.getHeight() - 70)), 'Click again to close')
    close.setSize(15)
    close.setTextColor('red')
    close.draw(win)

    #Waits for another click to exit
    win.getMouse()
    win.close()

def process_string():
    user_input = str(input("Type something: "))
    first_char = user_input[0]
    last_char = user_input[-1]
    print(first_char, last_char)

def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = str(values[1] + values[3])
    print(x)
    x = values[0] + values[2]
    print(x)
    x = str(values[1] * values[0])
    print(x)
    x = list([values[2], values[3], pt])
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = list([values[2], values[0], float(values[-1])])
    print(x)
    x = values[0] + values[2] + float(values[-1])
    print(x)
    x = len(values)
    print(x)
process_list()

def another_series():
    terms = eval(input("Enter number of terms to sum:"))
    sum = 0
    series = 0
    for i in range(terms):
        series = series + 2
        sum = sum + series
        series = series % 6
    print(sum)

def target():
    win = GraphWin('Archery Window', 500, 500)

    # White Ring
    white = Circle(Point((win.getWidth() / 2), (win.getHeight() / 2)), 248)
    white.setFill('white')
    white.draw(win)

    # Black Ring
    black = Circle(Point((win.getWidth() / 2), (win.getHeight() / 2)), 198)
    black.setFill('black')
    black.draw(win)

    # Blue Ring
    blue = Circle(Point((win.getWidth() / 2), (win.getHeight() / 2)), 148)
    blue.setFill('blue')
    blue.draw(win)

    # Red Ring
    red = Circle(Point((win.getWidth() / 2), (win.getHeight() / 2)), 98)
    red.setFill('red')
    red.draw(win)

    # Yellow Ring - Bullseye
    bullseye = Circle(Point((win.getWidth() / 2), (win.getHeight() / 2)), 48)
    bullseye.setFill('yellow')
    bullseye.draw(win)

    time.sleep(1)

    # Instructions to close window
    close = Text(Point((win.getWidth() / 2), (win.getHeight() - 30)), 'Click again to close')
    close.setSize(30)
    close.setTextColor('red')
    close.draw(win)

    win.getMouse()
    win.close()
