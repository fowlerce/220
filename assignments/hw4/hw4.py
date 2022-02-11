"""
Name: Christian Fowler
hw4.py

Problem: Creates graphics windows and solves for pi.

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""

import math

from graphics import *


def squares():
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    num_clicks = 5

    instructions = Text(Point(200, 390), "Click to draw new squares")
    instructions.setTextColor('red')
    instructions.draw(win)

    shape = Rectangle(Point(50, 50), Point(100, 100))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    for i in range(num_clicks):
        click = win.getMouse()
        new_center = shape.getCenter()
        dx = click.getX() - new_center.getX()
        dy = click.getY() - new_center.getY()
        new_square = shape.clone()
        new_square.move(dx, dy)
        new_square.draw(win)

    close = Text(Point(200, 370), 'Click again to close')
    close.setTextColor('red')
    close.draw(win)

    win.getMouse()
    win.close()

def rectangle():
    win = GraphWin('Window', 500, 500)

    corner1 = win.getMouse()
    corner2 = win.getMouse()

    rectangle = Rectangle(corner1, corner2)
    rectangle.setOutline('green')
    rectangle.setFill('green')
    rectangle.draw(win)

    x1 = corner1.getX()
    y1 = corner1.getY()
    x2 = corner2.getX()
    y2 = corner2.getY()
    length = abs(x1 - x2)
    width = abs(y1 - y2)
    perimeter_calc = float((length * 2)) + float((width * 2))
    area_calc = float(length * width)

    perimeter_message = Text(Point((win.getWidth() / 2), (win.getHeight() - 40)), 'Perimeter: {}'.format(perimeter_calc))
    perimeter_message.setSize(15)
    perimeter_message.setFill('red')
    perimeter_message.draw(win)

    area_message = Text(Point((win.getWidth() / 2), (win.getHeight() - 20)), 'Area: {}'.format(area_calc))
    area_message.setSize(15)
    area_message.setFill('red')
    area_message.draw(win)

    time.sleep(1)

    close = Text(Point((win.getWidth() / 2), (win.getHeight() - 60)), 'Click again to close')
    close.setSize(15)
    close.setTextColor('red')
    close.draw(win)

    win.getMouse()
    win.close()

def circle():
    win = GraphWin('Window', 500, 500)

    center = win.getMouse()
    center_pt = Point(center.getX(), center.getY())
    edge = win.getMouse()
    radx = (edge.getX() - center.getX())**2
    rady = (edge.getY() - center.getY())**2
    rad = math.sqrt((radx + rady))

    circle = Circle(center_pt, rad)
    circle.setOutline('blue')
    circle.setFill('blue')
    circle.draw(win)

    rad_prompt = Text(Point((win.getWidth() / 2), (win.getHeight() - 20)), 'Radius: {}'.format(rad))
    rad_prompt.setSize(15)
    rad_prompt.setFill('red')
    rad_prompt.draw(win)

    time.sleep(1)

    close = Text(Point((win.getWidth() / 2), (win.getHeight() - 40)), 'Click again to close')
    close.setSize(15)
    close.setFill('red')
    close.draw(win)

    win.getMouse()
    win.close()

def pi2():
    num = 4
    den = 1
    solution = 0
    terms = eval(input("Enter number of terms to sum: "))
    for i in range(terms):
        fraction = (num / den)
        solution = solution + fraction
        num = num * (-1)
        den = den + 2
    approx = 'Pi Approximation: {}'.format(solution)
    accuracy = 'Accuracy: {}'.format(abs(math.pi - solution))
    print(approx)
    print(accuracy)

if __name__ == '__main__':
    pass
