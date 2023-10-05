import random


class Dice:
    # Attributes
    number_of_faces = 0
    pips = 0




    # Constructor
    def __init__(self,number_of_faces, pips):
        self.number_of_faces = number_of_faces
        self.pip = pips


    # Methods
    def roll():
        dice = random.randint(1,6)
        return dice

    def display_num():
        return

class Player:
    # Attributes
    name = ""
    turn = 0


    # Constructor
    def __init__(self, name):
        self.name = name

    # Methods
    def play():
        return


class Board:
    # Atributes
    color = ""


    # Constructor
    def __init__(self, color):
        self.color = color

    # Methods 
    def switch():
        return   