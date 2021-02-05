from turtle import Turtle
from time import sleep

# y position of cars will be randomized in between the viable area so between -350 and 350.
SPEED = 3


class Car(Turtle):

    def __init__(self):
        super(Car, self).__init__()
        self.penup()
        self.goto(x=1200, y=0)
        self.speed(SPEED)

    def move(self):
        self.fd(10)

    def speed_incrementation(self):
        global SPEED
        SPEED += 1
        self.speed(SPEED)
