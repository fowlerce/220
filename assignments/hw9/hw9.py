"""
Name: Christian Fowler
hw9.py

Problem: Hangman

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""

import random
from graphics import *


def get_words(file_name):
    word_file = open(file_name, 'r')
    word_list = word_file.readlines()
    return word_list


def get_random_word(word_list):
    secret_word = random.choice(list(word_list)).strip()
    return secret_word


def letter_in_secret_word(letter, secret_word):
    check_letter = str(secret_word).find(str(letter))
    if check_letter == -1:
        return False
    else:
        return True


def already_guessed(letter, guesses):
    if str(guesses).find(letter) == -1:
        return False
    else:
        return True


def make_hidden_secret(secret_word, guesses):
    correct_guesses = []
    spaces = str('_ ' * len(secret_word)).split()
    for i in str(guesses):
        if i in secret_word:
            occurences = secret_word.count(i)
            for j in range(occurences):
                correct_guesses += i
    for letter in correct_guesses:
        index = str(secret_word).find(letter)
        if index in range(len(secret_word)) != -1:
            spaces[index] = secret_word[index]
        else:
            spaces[index] = '_'
    output = ' '.join(spaces)
    return output


def won(guessed):
    check_game = guessed.find('_')
    if not check_game:
        return False
    else:
        return True


def play_command_line(secret_word):
    list_of_guesses = []
    secret_spaces = make_hidden_secret(secret_word, list_of_guesses)
    chances = 6
    while not won(secret_spaces) and chances != 0:
        user_guess = input('Guess a letter: ')
        list_of_guesses.append(user_guess)
        check = letter_in_secret_word(user_guess, secret_word)
        guessed_already = already_guessed(user_guess, list_of_guesses)
        if not guessed_already and check:
            make_hidden_secret(secret_word, list_of_guesses)
        else:
            chances = chances - 1


def play_graphics(secret_word):
    # Creates window:
    width = 750
    height = 750
    win = GraphWin("Hangman", width, height)
    win.setBackground("black")

    # Creates "chances remaining" text area:
    chances_remaining = 6
    chances_text_area = Rectangle(Point(0, 0), Point(375, 100))
    chances_text_area.setOutline('white')
    chances_text_area.draw(win)
    chances_text_label = Text(Point(187.5, 25), 'Chances Remaining:')
    chances_text_label.setOutline('white')
    chances_text_label.setSize(15)
    chances_text_label.draw(win)
    display_chances = Text(Point(187.5, 60), 6)
    display_chances.setOutline('red')
    display_chances.setSize(30)
    display_chances.draw(win)

    # Creates "letters already guessed" text area:
    guesses = []
    guesses_text_area = Rectangle(Point(375, 0), Point(750, 100))
    guesses_text_area.setOutline('white')
    guesses_text_area.draw(win)
    guesses_text_label = Text(Point(562.5, 25), 'Already Guessed:')
    guesses_text_label.setOutline('white')
    guesses_text_label.setSize(15)
    guesses_text_label.draw(win)
    display_guesses = Text(Point(562.5, 60), guesses)
    display_guesses.setOutline('red')
    display_guesses.setSize(30)

    # Creates user entry input box
    guess_instructions = Text(Point(375, 635), 'Guess a letter: ')
    guess_instructions.setOutline('white')
    guess_instructions.setSize(25)
    guess_instructions.draw(win)
    user_entry = Entry(Point(375, 670), 20)
    user_entry.setFill('white')
    user_entry.draw(win)

    # Creates class 'button' for submitting guesses:
    class button:
        def __init__(self, shape, color, label):
            self.shape = shape
            self.color = color
            self.text = Text(shape.getCenter(), label)
        def set_label(self, label):
            self.text.setText(label)
        def set_color(self, color):
            self.shape.setFill(color)
        def is_clicked(self, point):
            upper_left = self.shape.getP1()
            lower_right = self.shape.getP2()
            if (upper_left.getX() <= point.getX() <= lower_right.getX()) and (
                    upper_left.getY() <= point.getY() <= lower_right.getY()):
                return True
            else:
                return False
        def draw(self, win):
            self.shape.draw(win)
            self.text.draw(win)
        def undraw(self):
            self.shape.undraw()
            self.text.undraw()
    button_shape = Rectangle(Point(335, 700), Point(415, 730))
    button_color = button_shape.setFill('white')
    submit_label = Text(Point(375, 715), 'Submit')
    submit_label.setOutline('black')
    submit_label.setSize(20)
    submit_button = button(button_shape, button_color, 'Submit')

    # Creates secret word spaces
    display_spaces = Text(Point(375, 450), ('_ ' * len(secret_word)))
    display_spaces.setOutline('white')
    display_spaces.setSize(35)
    display_spaces.draw(win)

    # Creates gallows:
    gallows_left_vert = Line(Point(50, 725), Point(50, 125))
    gallows_left_vert.setOutline('white')
    gallows_left_vert.setWidth(10)
    gallows_left_vert.draw(win)
    gallows_right_vert = Line(Point(700, 725), Point(700, 125))
    gallows_right_vert.setOutline('white')
    gallows_right_vert.setWidth(10)
    gallows_right_vert.draw(win)
    gallows_top = Line(Point(15, 125), Point(735, 125))
    gallows_top.setOutline('white')
    gallows_top.setWidth(10)
    gallows_top.draw(win)
    gallows_left_support = Line(Point(50, 200), Point(175, 125))
    gallows_left_support.setOutline('white')
    gallows_left_support.setWidth(10)
    gallows_left_support.draw(win)
    gallows_right_support = Line(Point(700, 200), Point(575, 125))
    gallows_right_support.setOutline('white')
    gallows_right_support.setWidth(10)
    gallows_right_support.draw(win)
    gallows_noose_vert = Line(Point(375, 125), Point(375, 250))
    gallows_noose_vert.setOutline('white')
    gallows_noose_vert.setWidth(7.5)
    gallows_noose_vert.draw(win)
    gallows_noose_loop = Circle(Point(375, 270), 20)
    gallows_noose_loop.setOutline('white')
    gallows_noose_loop.setWidth(7.5)
    gallows_noose_loop.draw(win)

    # Creates body parts
    head = Circle(Point(375, 270), 20)
    head.setOutline('red')
    head.setWidth(5)
    torso = Line(Point(375, 290), Point(375, 365))
    torso.setOutline('red')
    torso.setWidth(5)
    left_arm = Line(Point(375, 300), Point(355, 335))
    left_arm.setOutline('red')
    left_arm.setWidth(5)
    right_arm = Line(Point(375, 300), Point(395, 335))
    right_arm.setOutline('red')
    right_arm.setWidth(5)
    left_leg = Line(Point(375, 365), Point(355, 395))
    left_leg.setOutline('red')
    left_leg.setWidth(5)
    right_leg = Line(Point(375, 365), Point(395, 395))
    right_leg.setOutline('red')
    right_leg.setWidth(5)

    # Creates error message:
    error_message = Text(Point(375, 525), 'You\'ve already guessed that letter!')
    error_message.setOutline('white')
    error_message.setSize(25)

    # Creates "game over" message:
    game_over = Text(Point(375, 50), 'Game over')
    game_over.setOutline('red')
    game_over.setSize(25)
    close = Text(Point(375, 75), 'Click anywhere to close')
    close.setOutline('red')
    close.setSize(15)

    # Runs game:
    while not won(display_spaces.getText()) and display_chances.getText() != 0:
        display_guesses.draw(win)
        submit_button.draw(win)
        if submit_button.is_clicked(win.getMouse()):
            if not already_guessed(user_entry.getText(), guesses):
                if letter_in_secret_word(user_entry.getText(), secret_word):
                    guesses.append(user_entry.getText())
                    display_spaces.undraw()
                    index = secret_word.find(user_entry.getText())
                    display_spaces.getText()[index] = user_entry.getText()
                elif display_chances.getText() == 6:
                    guesses.append(user_entry.getText())
                    head.draw(win)
                    display_chances.undraw()
                    display_chances = Text(Point(187.5, 60), 5)
                    display_chances.setOutline('red')
                    display_chances.setSize(30)
                    display_chances.draw(win)
                elif display_chances.getText() == 5:
                    guesses.append(user_entry.getText())
                    torso.draw(win)
                    display_chances.undraw()
                    display_chances = Text(Point(187.5, 60), 4)
                    display_chances.setOutline('red')
                    display_chances.setSize(30)
                    display_chances.draw(win)
                elif display_chances.getText() == 4:
                    guesses.append(user_entry.getText())
                    left_arm.draw(win)
                    display_chances.undraw()
                    display_chances = Text(Point(187.5, 60), 3)
                    display_chances.setOutline('red')
                    display_chances.setSize(30)
                    display_chances.draw(win)
                elif display_chances.getText() == 3:
                    guesses.append(user_entry.getText())
                    right_arm.draw(win)
                    display_chances.undraw()
                    display_chances = Text(Point(187.5, 60), 2)
                    display_chances.setOutline('red')
                    display_chances.setSize(30)
                    display_chances.draw(win)
                elif chances_remaining == 2:
                    guesses.append(user_entry.getText())
                    left_leg.draw(win)
                    display_chances.undraw()
                    display_chances = Text(Point(187.5, 60), 1)
                    display_chances.setOutline('red')
                    display_chances.setSize(30)
                    display_chances.draw(win)
                elif chances_remaining == 1:
                    guesses.append(user_entry.getText())
                    right_leg.draw(win)
                    display_chances.undraw()
                    display_chances = Text(Point(187.5, 60), 0)
                    display_chances.setOutline('red')
                    display_chances.setSize(30)
                    display_chances.draw(win)
            else:
                for reps in range(3):
                    error_message.draw(win)
                    time.sleep(.5)
                    error_message.undraw()
                    time.sleep(.5)
        display_guesses.undraw()
        submit_button.undraw()

    chances_text_area.undraw()
    chances_text_label.undraw()
    guesses_text_area.undraw()
    guesses_text_label.undraw()
    display_guesses.undraw()
    guess_instructions.undraw()
    user_entry.undraw()
    submit_button.undraw()
    submit_label.undraw()
    game_over.draw(win)
    close.draw(win)
    win.getMouse()
    win.close()


def main():
    words_list = get_words("words.txt")
    secret_word = get_random_word(words_list)
    play_command_line(secret_word)
    play_graphics(secret_word)


if __name__ == '__main__':
    main()
