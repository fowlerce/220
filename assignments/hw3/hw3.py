"""
Name: Christian Fowler
hw3.py

Problem: Provides various mathematical functions utilizing loops.

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""
import math


def average():
    inputs = eval(input("How many grades will you enter? "))
    sum = 0
    for i in range(inputs):
        grades = eval(input("Enter grade: "))
        sum = sum + grades
    avg = sum / inputs
    print("Average is", avg)


def tip_jar():
    total = 0
    for i in range(5):
        tip = eval(input("How much would you like to donate? "))
        total = total + tip
    print("Total tips:", total)


def newton():
    x = eval(input("What number do you want to square root? "))
    approx = eval(input("How many times do you want to improve the approximation? "))
    for i in range(approx):
        approx = 0.5 * (approx + x / approx)
    print("The square root is approximately", approx)


def sequence():
    terms = int(input("How many terms would you like? "))
    output = []
    for i in range(1, terms + 1, 2):
        output.append(i)
        output.append(i)
    for j in range(0, terms):
        print(str(output[j]) + " ", end="")

        
## In referece to pi() and newton() --->
## I've tried everything I can possibly think of
## I've used every mathematical method I can muster - and I keep getting the same answer of 2.844(...) for the first example
## I can't find anything that works without 'if' or 'while'
## It's really dumb
## I want to put my head through my computer screen


def pi():
    pi = 2
    terms = eval(input("How many terms are in the series?"))
    for i in range(1, terms):
        num = (2 * i)/(2 * i - 1)
        den = (2 * i)/(2 * i +1)
        pi = pi * num * den
    print(pi)

if __name__ == '__main__':
    pass
