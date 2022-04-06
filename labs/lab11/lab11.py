"""
Name: Christian Fowler
lab11.py

Problem: Three Door Game II

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""

'''
I have the doors set to 'brown,' yet they seem more red than brown.

However, if I set them to yellow (or any other color), they are very yellow.

That being said, when the program colors a door red, you can still tell a
distinct difference between the 'brown' and red.
'''


from labs.lab10.button import Button
from labs.lab10.door import Door
from graphics import *
from random import randint

def main():
    width = 750
    height = 750
    win = GraphWin("Three Door Game", width, height)
    win.setBackground("light blue")

    # Displays wins/losses
    class Wins:
        def __init__(self, shape, label):
            self.shape = shape
            self.text = Text(shape.getCenter(), label)
        def draw(self, win):
            self.shape.draw(win)
            self.text.draw(win)
        def undraw(self):
            self.shape.undraw()
            self.text.undraw()
        def set_label(self, label):
            self.text.setText(label)

    class Losses:
        def __init__(self, shape, label):
            self.shape = shape
            self.text = Text(shape.getCenter(), label)
        def draw(self, win):
            self.shape.draw(win)
            self.text.draw(win)
        def undraw(self):
            self.shape.undraw()
            self.text.undraw()
        def set_label(self, label):
            self.text.setText(label)

    num_of_wins = 0
    wins_shape = Rectangle(Point(75, 35), Point(150, 110))
    wins_shape.setOutline('black')
    wins_title = Text(Point(112.5, 20), 'Wins')
    wins_title.setOutline('black')
    wins_title.setSize(15)
    wins_title.draw(win)
    wins = Wins(wins_shape, num_of_wins)
    wins.draw(win)

    num_of_losses = 0
    losses_shape = Rectangle(Point(150, 35), Point(225, 110))
    losses_shape.setOutline('black')
    losses_title = Text(Point(187.5, 20), 'Losses')
    losses_title.setOutline('black')
    losses_title.setSize(15)
    losses_title.draw(win)
    losses = Losses(losses_shape, num_of_losses)
    losses.draw(win)

    # Displays quit button
    button_shape = Rectangle(Point(525, 35), Point(675, 110))
    quit = Button(button_shape, 'Quit')
    quit.draw(win)

    # Displays doors
    door1_shape = Rectangle(Point(75, 200), Point(225, 600))
    door1_shape.setOutline('black')
    door1 = Door(door1_shape, 'Door 1')
    door1.draw(win)

    door2_shape = Rectangle(Point(300, 200), Point(450, 600))
    door2_shape.setOutline('black')
    door2 = Door(door2_shape, 'Door 2')
    door2.draw(win)

    door3_shape = Rectangle(Point(525, 200), Point(675, 600))
    door3_shape.setOutline('black')
    door3 = Door(door3_shape, 'Door 3')
    door3.draw(win)

    # Displays instructions and messages
    header = Text(Point(375, 155), 'I have a secret door')
    header.setOutline('black')
    header.setSize(15)
    header.draw(win)

    footer = Text(Point(375, 675), 'Click to guess which is the secret door!')
    footer.setOutline('black')
    footer.setSize(15)
    footer.draw(win)

    incorrect_message = Text(Point(375, 155), 'Sorry, that\'s incorrect!')
    incorrect_message.setOutline('black')
    incorrect_message.setSize(15)

    win_message = Text(Point(375, 155), 'You win!')
    win_message.setOutline('black')
    win_message.setSize(25)

    play_again = Text(Point(375, 675), 'Click anywhere to play again!')
    play_again.setOutline('black')
    play_again.setSize(25)

    try_again = Text(Point(375, 155), 'Click on a door to guess! Try again!')
    try_again.setOutline('black')
    try_again.setSize(25)

    door_list = [door1, door2, door3]
    int = randint(0, 2)
    door_list[int].set_secret(True)

    # Runs game
    for game in range(1):
        door1.color_door('brown')
        door2.color_door('brown')
        door3.color_door('brown')

        mouse = win.getMouse()

        if quit.is_clicked(mouse):
            win.close()

        else:
            while not quit.is_clicked(mouse):
                door1.color_door('brown')
                door2.color_door('brown')
                door3.color_door('brown')

                header.undraw()
                footer.undraw()
                header.draw(win)
                footer.draw(win)

                mouse = win.getMouse()

                door_list = [door1, door2, door3]
                int = randint(0, 2)
                door_list[int].set_secret(True)

                if door_list[int].is_clicked(mouse):
                    num_of_wins = num_of_wins + 1
                    wins.set_label(num_of_wins)

                    door_list[int].color_door('green')

                    header.undraw()
                    win_message.draw(win)

                    footer.undraw()
                    play_again.draw(win)

                elif door_list[int - 1].is_clicked(mouse):
                    door_list[int - 1].color_door('red')
                    door_list[int].color_door('green')

                    num_of_losses = num_of_losses + 1
                    losses.set_label(num_of_losses)

                    header.undraw()
                    incorrect_message.draw(win)

                    footer.undraw()
                    play_again.draw(win)

                elif door_list[int - 2].is_clicked(mouse):
                    door_list[int - 2].color_door('red')
                    door_list[int].color_door('green')

                    num_of_losses = num_of_losses + 1
                    losses.set_label(num_of_losses)

                    header.undraw()
                    incorrect_message.draw(win)

                    footer.undraw()
                    play_again.draw(win)

                elif quit.is_clicked(mouse):
                    win.close()

                else:
                    header.undraw()
                    try_again.draw(win)
                    footer.undraw()
                    play_again.draw(win)

                # Clears all current on-screen message
                mouse = win.getMouse()

                if quit.is_clicked(mouse):
                    win.close()

                try_again.undraw()
                play_again.undraw()
                incorrect_message.undraw()
                win_message.undraw()
                header.draw(win)
                footer.draw(win)

                # Chooses new secret door
                int = randint(0, 2)
                door_list[int].set_secret(True)

            win.close()
