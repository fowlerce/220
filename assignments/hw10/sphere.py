"""
Name: Christian Fowler
sphere.py

Problem: Creates Class 'Sphere'

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""

import math


class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def surface_area(self):
        surf_area = 4 * math.pi * self.radius**2
        return surf_area

    def volume(self):
        volume = (4/3) * math.pi * self.radius**3
        return volume
