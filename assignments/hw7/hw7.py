"""
Name: Christian Fowler
hw7.py

Problem: Working with files and functions

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""


def number_words(test1, out_file_name):
    in_file = open(test1, "r")
    out_file = open(out_file_name, "w")
    text_in = in_file.read().split()
    counter = 1
    for i in range(len(text_in)):
        print(counter, text_in[i], file = out_file)
        counter = counter + 1
    in_file.close()
    out_file.close()

def hourly_wages(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")
    for line in in_file:
        splitter = line.split(' ')
        bonus_pay = eval(splitter[2]) + 1.65
        weekly_pay = bonus_pay * eval(splitter[3])
        print('{}{}{}{}{:.2f}'.format(splitter[0], ' ', splitter[1], ' ', weekly_pay), file = out_file)
    in_file.close()
    out_file.close()

def calc_check_sum(isbn):
    position = 10
    sum = 0
    for digit in isbn:
        try:
            product = eval(digit) * position
            sum = sum + product
            position = position - 1
        except:
            pass
    return sum

def send_message(file_name, friend_name):
    in_file = open(file_name, "r")
    out_file = open('{}.txt'.format(friend_name), "w")
    text = in_file.read()
    out_file.write(text)
    in_file.close()
    out_file.close()

def send_safe_message(file_name, friend_name, key):
    from encryption import encode
    in_file = open(file_name, "r")
    out_file = open('{}.txt'.format(friend_name), "w")
    raw_text = in_file.read()
    splitter = raw_text.split('\n')
    for line in splitter:
        message = line
        encrypt_text = encode(message, key)
        print(encrypt_text.rstrip(), file=out_file)
    in_file.close()
    out_file.close()
#Correct output, but failing the tests

def send_uncrackable_message(file_name, friend_name, pad_file_name):
    from encryption import encode_better
    in_file = open(file_name, "r")
    pad = open(pad_file_name, "r")
    raw_text = in_file.read()
    encrypt_text = encode_better(raw_text, pad)
#Incomplete

if __name__ == '__main__':
    pass
