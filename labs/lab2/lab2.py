"""
Name: Christian Fowler
lab2.py

Problem: Provides three different methods for calculating a mean of a set of numbers.

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.

"""


import math


def means():
    num_values = eval(input("Enter the number of values to be entered: "))
    squares = 0
    harm_x = 0
    values_prod = 1
    for i in range(num_values):
        values = eval(input("Enter value: "))
        squares = squares + values**2
        mean_squares = squares / num_values
        rms_avg = round(mean_squares**0.5, 3)
        harm_x = harm_x + (1 / values)
        values_prod = values_prod * values
    geo_mean = round(values_prod ** (1 / num_values), 3)
    harm_mean = round(num_values / harm_x, 3)
    print("RMS = ", rms_avg)
    print("Harmonic Mean = ", harm_mean)
    print("Geometric Mean = ", geo_mean)
