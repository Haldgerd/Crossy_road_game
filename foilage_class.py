from turtle import Turtle
from random import choice


# ------- GLOBAL VARIABLES --------
FOLIAGE_SHAPES = ["./Images/tree-1.gif", "./Images/tree-2.gif", "./Images/tree-3.gif", "./Images/tree-4.gif",
                  "./Images/tree-5.gif", "./Images/tree-6.gif"]  # pictures [.gif format] of 12 trees.


class Foliage:

    def __init__(self):
        self.foliage = []
        self.create_foliage_down()
        self.create_foliage_up()

    def create_foliage_down(self):
        """
        Creates 12 different tree objects with different graphics, placed by the road.
        :return: self.foliage, list of tree objects.
        """
        x = -500
        y = -350
        for shape in range(6):
            tree = Turtle()
            tree.penup()
            tree.shape(choice(FOLIAGE_SHAPES))
            tree.setpos(x=x, y=y)
            self.foliage.append(tree)
            x += 200

    def create_foliage_up(self):
        x = -500
        y = 380
        for shape in range(6):
            tree = Turtle()
            tree.penup()
            tree.shape(choice(FOLIAGE_SHAPES))
            tree.setpos(x=x, y=y)
            self.foliage.append(tree)
            x += 200
