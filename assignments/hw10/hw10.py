"""
Name: Christian Fowler
hw10.py

Problem: More loops

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""


def fibonacci(int):
    counter = 3
    previous = 1
    current = 1
    sum = 0

    if int < 1:
        return None
    else:
        while counter <= int:
            counter = counter + 1
            sum = previous + current
            previous = current
            current = sum
    return sum


def double_investment(principle, rate):
    years = 0
    double_principal = principle * 2
    while principle <= double_principal:
        a = principle * (1 + rate)
        principle = a
        years = years + 1
    return years


def syracuse(int):
    output = [int]
    while int != 1:
        if int % 2 == 0:
            int = int / 2
            output.append(int)
        elif int % 2 != 0:
            int = 3 * int + 1
            output.append(int)
    return output


def goldbach(n):
    num_range = set(range(n, 1, -1))
    primes_list = []
    output = []
    while num_range:
        pop = num_range.pop()
        primes_list.append(pop)
        num_range.difference_update(set(range(pop * 2, n + 1, pop)))
    primes_list = primes_list[1:]

    x = 0
    y = 1
    if n % 2 != 0:
        return None
    else:
        while x < len(primes_list):
            while y < len(primes_list):
                if primes_list[x] + primes_list[y] == n:
                    output.append(primes_list[x])
                    output.append(primes_list[y])
                    break
                else:
                    y = y + 1
            x = x + 1
            y = x + 1
        return output[:2]
