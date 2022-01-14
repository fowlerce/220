"""
Name: Christian Fowler
hw1.py

Problem: Provides functions and calculations for different formulas.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)


def shooting_percentage():
    total = eval(input("Enter the player's total shots: "))
    made = eval(input("Enter how many shots the player made: "))
    percentage = made / total
    print("Shooting Percentage:", percentage)


def coffee():
    pounds = eval(input("How many pounds of coffee would you like? "))
    cost = 10.5 * pounds
    shipping = 0.86 * pounds
    overhead = 1.5
    total = cost + shipping + overhead
    print("Your total is:", total)


def kilometers_to_miles():
    kilometers = eval(input("How many kilometers did your travel? "))
    miles = kilometers / 1.61
    print("That's", miles, "miles!")


if __name__ == '__main__':
    pass
