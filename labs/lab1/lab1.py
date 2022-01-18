"""
Name: Christian Fowler

File: lab1.py

Problem Description: Calculates monthly interest on a credit card

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""


def monthly_interest():
    apr = (eval(input("Enter annual interest rate (APR): "))) / 100
    print(apr)
    days = eval(input("Enter number of days in the billing cycle: "))
    prevbal = eval(input("Enter previous balance: "))
    payamount = eval(input("Enter payment amount: "))
    payday = eval(input("Enter day of billing cycle when payment was made: "))
    step_1 = prevbal * days
    step_2 = payamount * (days - payday)
    step_3 = step_1 - step_2
    dailybalance = step_3 / days
    monthlyinterest = dailybalance * (apr / 12)
    print("Your total monthly interest is: ", monthlyinterest)