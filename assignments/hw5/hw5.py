"""
Name: Christian Fowler
hw5.py

Problem: Continues practice with strings and lists.

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""

def name_reverse():
    name = str(input("Enter a name (first & last): "))
    splitter = name.split(" ")
    output = '{}, {}'.format(splitter[1], splitter[0])
    print(output)

def company_name():
    url = input("Enter a domain")
    parts = url.split(".")
    print(parts[1])

def initials():
    students = eval(input("How many students are in the class?"))
    count = 0
    for i in range(students):
        count = count + 1
        name = input("What is the name of student {}{}".format(count, "?"))
        name_split = name.split(" ")
        first = name_split[0]
        last = name_split[1]
        first_initial = first[0]
        last_initial = last[0]
        print('{}{}'.format(first_initial, last_initial))

def names():
    names = input("Enter a list of names (first and last), separated by commas:")
    splitter = names.split(" ")
    for i in range(0, len(splitter), 2):
        first = splitter[i]
        first_initial = first[0]
        last = splitter[i+1]
        last_initial = last[0]
        print('{}{}'.format(first_initial, last_initial))

def thirds():
    counter = 0
    terms = eval(input("Enter the number of sentences:"))
    output = []
    for i in range(terms):
        counter = counter + 1
        sentence = input("Enter Sentence {}:".format(counter))
        output.append(sentence)
    for j in range(0, len(output)):
        third = output[j][0::3]
        print(third)

def word_average():
    sentence = input("Enter a sentence:")
    splitter = sentence.split(" ")
    sum = 0
    for i in range(len(splitter)):
        char_count = len(splitter[i])
        sum = sum + char_count
    avg = sum / len(splitter)
    print(avg)

def pig_latin():
    sentence = input("Enter a sentence to convert to pig latin:")
    splitter = sentence.split(" ")
    for i in range(len(splitter)):
        word = splitter[i]
        shift = '{}{}{}'.format(word[1:], word[0], 'ay')
        splitter[i] = shift
        translated = ' '.join(splitter)
    print(translated.lower())


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
