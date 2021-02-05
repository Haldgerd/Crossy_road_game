from turtle import Turtle
from time import sleep

DISTANCE = 20


class Frog(Turtle):

    def __init__(self):
        super(Frog, self).__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=-410)
        self.showturtle()
        self.shape("turtle")
        self.setheading(90)

    def move(self):
        self.forward(DISTANCE)

    def reset_frog(self):
        self.hideturtle()
        self.goto(x=0, y=-410)
        self.setheading(90)
        self.showturtle()