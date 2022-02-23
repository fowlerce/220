"""
Name: Christian Fowler
lab6.py

Problem: ATTEMPTS to implement the Vigenere cipher, but fails.

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""

from graphics import *

def vigenere():
    # -------------------------# Beginning of GUI process #-------------------------#
    width = 500
    height = 500
    win = GraphWin("Vigenere", width, height)

    # Graphical User Interface Box
    gui = Rectangle(Point(10, 10), Point((win.getWidth() - 10), (win.getHeight() - 10)))
    gui.setFill('gray85')
    gui.setOutline('black')

    # Instructions
    message_inst = Text(Point((win.getWidth() - win.getWidth() * 0.6875), (win.getHeight() // 4)), "Message to encode:")
    message_inst.setSize(15)
    keyword_inst = Text(Point((win.getWidth() - win.getWidth() * 0.6875), (win.getHeight() // 4) + 60), "Enter Keyword:")
    keyword_inst.setSize(15)

    # Entry Objects
    message_entry = Entry(Point((win.getWidth() - win.getWidth() * 0.3125), (win.getHeight() // 4)), 25)
    keyword_entry = Entry(Point((win.getWidth() - win.getWidth() * 0.3125), (win.getHeight() // 4) + 60), 25)

    # Button (not functional - only for looks)
    button = Rectangle(Point((win.getWidth() // 2) - 40, (win.getHeight() // 2) - 20), Point((win.getWidth() // 2) + 40, (win.getHeight() // 2) + 20))
    button.setFill('white')

    button_inst = Text(Point((win.getWidth() // 2), (win.getHeight() // 2)), "Encode")
    button_inst.setSize(15)

    # Draw
    gui.draw(win)
    message_inst.draw(win)
    message_entry.draw(win)
    keyword_inst.draw(win)
    keyword_entry.draw(win)
    button.draw(win)
    button_inst.draw(win)

    # Wait for user click
    win.getMouse()

    #-------------------------# Beginning of encoding process #-------------------------#

    # Retrieves & cleans text input
    message = message_entry.getText().upper().replace(' ', '')
    keyword = keyword_entry.getText().upper()

    #message_list = []
    #keyword_list = []
    #encoded_list = []

    #output = ''

    # Loops through inputs
    #for x in message:
    #    message_value = ord(x) - 65
    #    message_list.append(message_value)
    #    print(message_value)

    #for y in keyword:
    #    keyword_value = ord(y) - 65
    #    keyword_list.append(keyword_value)
    #    print(keyword_value)

    #for x in message_list:
    #    enc_add = message_list[x] + keyword_list[x]
    #    enc_mod = enc_add % 26
    #    encoded_list.append(enc_mod)
    #    print(enc_mod)

    #for z in encoded_list:
    #    enc_char = z % 26
    #    output = output + chr(enc_char)
    #    print(output)

    # Deletes button & displays encoded message
    button.undraw()
    button_inst.undraw()

    results_intro = Text(Point((win.getWidth() // 2), (win.getHeight() // 2)), "Resulting Message:")
    results_intro.setSize(15)
    results = Text(Point((win.getWidth() // 2), (win.getHeight() // 2 + 20)), 'Jeffery Epstein didn\'t kill himself')
    results.setSize(15)

    results_intro.draw(win)
    results.draw(win)

    # Closes window
    close = Text(Point((win.getWidth() / 2), (win.getHeight() - 45)), 'Click Anywhere to Close Window')
    close.setSize(15)
    close.draw(win)
    win.getMouse()
    win.close()
