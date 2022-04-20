"""
Name: Christian Fowler
lab13.py

Problem: Analyzes the stock market for exchange volume that meets certain criteria

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""

# import algorithms
# from algorithms import *
# from lab12 import algorithms
# from labs import lab12.algorithms
# from labs.lab12 import algorithms
# from labs.lab12.algorithms import *

'''
I hope this^ isn't a silly mistake, but I CAN NOT successfully import algorithms.py.
I have tried everything I can think of, as well as everything other people have told me to try.
'''


def trade_alert(filename):
    hour_data = open(filename, 'r')
    hour = hour_data.readlines()
    hour = hour[0].split()
    seconds = 0
    print('Test: ', hour[171], hour[260], hour[289], hour[652], hour[776], hour[317], hour[571], hour[1182])
    while seconds <= len(hour) - 1:
        if eval(hour[seconds]) == 500:
            output = '{}{}{}'.format('ALERT: At second ', seconds, ' exactly 500 trades occurred.')
            seconds += 1
            print(output)
        elif eval(hour[seconds]) > 830:
            output = '{}{}{}'.format('WARNING: At second ', seconds, ' more than 830 trades occurred.')
            seconds += 1
            print(output)
        else:
            seconds += 1
    hour_data.close()


# if __name__ == '__main__':
    # trade_alert('trades.txt')
