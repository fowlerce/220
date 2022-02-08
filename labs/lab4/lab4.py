"""
Name: Christian Fowler
lab4.py

Problem: Displays a heart with an arrow shooting through it.

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""

from graphics import *
def heart():
    win = GraphWin('Window', 200, 150)

    left = Circle(Point(70, 70), 20)
    left.setWidth(3)
    left.setFill('red')
    left.setOutline('red')
    left.draw(win)

    right = Circle(Point(110, 70), 20)
    right.setWidth(3)
    right.setFill('red')
    right.setOutline('red')
    right.draw(win)

    base = Polygon([Point(50, 75), Point(90, 130), Point(130, 75)])
    base.setWidth(3)
    base.setFill('red')
    base.setOutline('red')
    base.draw(win)

    greeting = Text(Point(90,90), 'Happy Valentines Day!')
    greeting.setSize(15)
    greeting.setFill('white')
    greeting.setOutline('white')
    greeting.draw(win)

    time.sleep(1)

    arrow = Line(Point(20,150), Point(50, 120))
    arrow.setWidth(2)
    arrow.setOutline('black')
    arrow.draw(win)

    for i in range(0,45):
        arrow.move(1,-1)

    time.sleep(1.5)

    close = Text(Point(90,140), 'Click Anywhere To Close')
    close.setSize(8)
    close.setFill('white')
    close.setOutline('white')
    close.draw(win)

    win.getMouse()
    win.close()

heart()
