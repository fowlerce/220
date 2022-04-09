"""
Name: Christian Fowler
face.py

Problem: Creates Class 'Face'

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""

from graphics import *


class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.window = window
        self.head = Circle(center, size)
        self.shock_size = 0.25 * size # In case this needs deleting
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)

        # Draw
        self.head.draw(window)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        self.mouth.draw(window)

    def smile(self):
        smile_point_1 = self.mouth.getP1()
        smile_point_2 = self.mouth.getP2()
        smile_center = self.mouth.getCenter()
        clone_smile_center = smile_center.clone()
        clone_smile_center.move = (7, smile_center / 2)
        smile_line_1 = Line(smile_point_1, clone_smile_center)
        smile_line_2 = Line(smile_point_2, clone_smile_center)

        # Draw
        smile_line_1.draw(self.window)
        smile_line_2.draw(self.window)


    def shock(self):
        shock_size = self.shock_size
        shock_center = self.mouth.getCenter()
        shock = Circle(shock_center, shock_size)

        # Draw
        shock.draw(self.window)

    def wink(self):
        wink_center = self.left_eye.getCenter()
        wink_x = wink_center.getX()
        wink_y = wink_center.getY()
        wink_radius = self.left_eye.getRadius()
        wink = Line(Point((wink_x - wink_radius), wink_y), Point((wink_x + wink_radius), wink_y))

        # Draw
        self.left_eye.undraw()
        wink.draw(self.window)

