"""
Name: Christian Fowler
hw6.py

Problem: Working with strings

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""
import math

def cash_converter():
    amount = input("Enter an integer:")
    splitter = amount.split('.')
    dollars = splitter[0]
    cents = splitter[1]
    print('${}.{:0<2}'.format(dollars, cents))

def encode():
    message = input("Enter a message:")
    key = eval(input("Enter a key:"))
    output = ''
    for letter in message:
        shift = ord(letter) + key
        secret = chr(shift)
        output = output + secret
    print(output)

def sphere_area(radius: float):
    s = float(4.0 * math.pi * (radius**2.0))
    return s

def sphere_volume(radius: float):
    v = float(4.0 / 3.0 * math.pi * (radius**3.0))
    return v

def sum_n(number):
    sum = 0
    for i in range(number + 1):
        sum = sum + i
    return sum

def sum_n_cubes(number):
    sum = 0
    for i in range(number + 1):
        cube = i**3
        sum = sum + cube
    return sum

def encode_better():
    message = input("Enter a message:")
    key = input("Enter a key:")
    output = ''
    for i in range(len(message)):
        shift = ((ord(message[i])) - 65) + ((ord(key[i % len(key)])) - 65)
        new_num = (shift % 58) + 65
        new_char = chr(new_num)
        output = output + new_char
    print(output)

if __name__ == '__main__':
    cash_converter()
    encode()
    res = sphere_area(13)
    print(res)
    res = sphere_volume(13)
    print(res)
    res = sum_n(100)
    print(res)
    res = sum_n_cubes(13)
    print(res)
    encode_better()
    pass
