from turtle import Turtle
from time import sleep

FONT = "Courier New"
COLOR = "SeaGreen"


class BorderText(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-580, y=-380)
        self.pensize(12)
        self.color(COLOR)
        self.pendown()

    def draw_border(self):
        for _ in range(4):
            self.fd(1160)
            self.left(90)
            self.penup()
            self.fd(760)
            self.left(90)
            self.pendown()

    def title(self):
        self.penup()
        self.goto(x=0, y=0)
        self.write("Frog Crossing", align="center", font=(FONT, 40, "bold"))
        sleep(2)
        self.clear()
