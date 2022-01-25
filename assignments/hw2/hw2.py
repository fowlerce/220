"""
Name: Christian Fowler
hw2.py

Problem: Calculates various types of mathematical equations.

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.

"""
import math


def sum_of_threes():
    bound = eval(input("What is the upper bound? "))
    sum = 0
    for i in range(0,bound + 3):
            if (i % 3 == 0):
                sum = sum + i
    print("Sum of threes is ", sum)


def multiplication_table():
    for i in range(1,11):
        print('\t')
        for j in range(1,11):
            print(i * j, end = '\t')


def triangle_area():
    a = eval(input("What is the length of side a? "))
    b = eval(input("What is the length of side b? "))
    c = eval(input("What is the length of side c? "))
    s = (a + b + c)/2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("The area is", area)


def sum_squares():
    lower = eval(input("Enter lower bound: "))
    upper = eval(input("Enter upper bound: "))
    sum = 0
    for i in range(lower, upper + 1):
        sum = sum + i**2
    print(sum)


def power():
    base = eval(input("Enter a base: "))
    exponent = eval(input("Enter an exponent: "))
    solution = base**exponent
    print(base, " ^ ", exponent, " = ", solution)



if __name__ == '__main__':
    pass
