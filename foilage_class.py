from turtle import Turtle


# ------- GLOBAL VARIABLES --------
FOLIAGE_SHAPES = []  # pictures [.gif format] of 12 trees.


class Foliage:

    def __init__(self):
        self.foliage = []
        self.create_foliage()

    def create_foliage(self):
        """
        Creates 12 different tree objects with different graphics, placed by the road.
        :return: self.foliage, list of tree objects.
        """
        x = -750
        y = -380
        for shape in range(len(FOLIAGE_SHAPES)):
            tree = Turtle()
            tree.penup()
            tree.shape(FOLIAGE_SHAPES[shape])
            if shape == 6:
                y = 380

            tree.setpos(x=x, y=y)
            self.foliage.append(tree)
            x += 200
