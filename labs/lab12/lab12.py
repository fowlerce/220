"""
Name: Christian Fowler
lab12.py

Problem: More while loops

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""

from random import randint


def find_and_remove(list, value):
    counter = 0
    found = False
    while counter <= (len(list) - 1) and not found:
        print(counter)
        if list[counter] == value:
            if type(value) == str:
                list.remove(list[counter])
                list[counter] = 'Christian'
                found = True
            elif type(value) == int or type(value) == float:
                list.pop(list[counter])
                list[counter] = 'Christian'
                found = True
        else:
            counter = counter + 1


def good_input():
    correct = False
    while not correct:
        guess = eval(input('Guess a number: '))
        if 10 >= guess >= 1:
            correct = True
            return guess
        elif guess < 1:
            print('That\'s too low!')
        elif guess > 10:
            print('That\'s too high!')


def num_digits():
    end = False
    while not end:
        num = eval(input('Enter a positive integer: '))
        if num > 0:
            calc_num = num
            counter = 0
            while calc_num != 0:
                calc_num = calc_num // 10
                counter = counter + 1
            print(counter)
        elif num <= 0:
            end = True


def hi_lo_game():
    random_number = randint(1, 100)
    chances = 1
    correct = False
    while chances <= 7 and not correct:
        guess = eval(input('Enter a positive integer between 1 and 100: '))
        if guess == random_number:
            correct = True
        elif guess > random_number:
            print('That\'s too high!')
            chances += 1
        elif guess < random_number:
            print('That\'s too low!')
            chances += 1
    if correct:
        print('{}{}{}'.format('You win in ', chances, ' guesses!'))
    else:
        print('{}{}{}'.format('Sorry, you lose. The number was ', random_number, '.'))

     
