"""
Name: Christian Fowler
lab10.py

Problem: Three Door Game

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""

############# Begin note
'''
# I have no idea what I'm supposed to do with the
is_secret() and set_secret() functions. The handout doesn't
offer a lot of clarification on the subject.
'''
############# End note

# Begin main file
from graphics import *
from button import Button
from door import Door


def main():
    width = 750
    height = 750
    win = GraphWin("Three Door Game", width, height)
    win.setBackground("gray")

    # Displays Button and Door
    button_shape = Rectangle(Point(186, 50), Point(563, 186))
    button = Button(button_shape, 'Exit')
    button.draw(win)
    door_shape = Rectangle(Point(186, 210), Point(563, 725))
    door_shape.setFill('red')
    door = Door(door_shape, 'Closed')
    door.draw(win)

    # "Opens and closes" door
    while not button.is_clicked(win.getMouse()):
        if door.is_clicked(win.getMouse()):
            door.undraw()
            door.draw(win)
            door.open('white', door.set_label('Open'))
            if door.is_clicked(win.getMouse()):
                door.undraw()
                door.draw(win)
                door.close('red', door.set_label('Closed'))

    # Closes window
    win.close()

main()
