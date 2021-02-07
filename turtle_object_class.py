from turtle import Turtle
from time import sleep

DISTANCE = 20


class Dog(Turtle):

    def __init__(self):
        super(Dog, self).__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=-380)
        self.showturtle()
        self.shape("turtle")
        self.setheading(90)

    def move(self):
        self.forward(distance=DISTANCE)

    def move_left(self):
        self.setheading(180)
        self.forward(distance=DISTANCE)

    def reset_player(self):
        self.hideturtle()
        self.goto(x=0, y=-380)
        self.setheading(90)
        self.showturtle()
