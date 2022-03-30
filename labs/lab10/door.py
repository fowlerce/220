from graphics import *


class Door:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)
        self.secret = False
    def get_label(self):
        return self.text.getText()
    def set_label(self, label):
        self.text.setText(label)
    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)
    def undraw(self):
        self.shape.undraw()
        self.text.undraw()
    def is_clicked(self, point):
        upper_left = self.shape.getP1()
        lower_right = self.shape.getP2()
        if (upper_left.getX() <= point.getX() <= lower_right.getX()) and (
                upper_left.getY() <= point.getY() <= lower_right.getY()):
            return True
        else:
            return False
    def open(self, color, label):
        self.shape.setFill(color)
        self.text = Text(self.shape.getCenter(), label)
    def close(self, color, label):
        self.shape.setFill(color)
        self.text = Text(self.shape.getCenter(), label)
    def color_door(self, color):
        self.shape.setFill(color)
    def is_secret(self):
        if self.secret == True:
            return True
        else:
            return False
    def set_secret(self, secret):
        self.secret = secret
        
