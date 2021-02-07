from turtle import Turtle
from time import sleep

FONT = "Courier New"
COLOR = "SeaGreen"
Y_COR = -280


class BorderTextRoad(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-590, y=-400)
        self.pensize(100)
        self.color(COLOR)

    def draw_border(self):
        self.pendown()
        for _ in range(4):
            self.fd(1160)
            self.left(90)
            self.penup()
            self.fd(800)
            self.left(90)
            self.pendown()

    def title(self):
        self.pensize(3)
        self.penup()
        self.goto(x=0, y=0)
        self.color("red3")
        self.write("Dog Crossing", align="center", font=(FONT, 40, "bold"))
        sleep(2)
        self.clear()

    def draw_road(self):
        global Y_COR
        self.pensize(4)

        for _ in range(4):
            self.goto(x=-590, y=Y_COR)
            if _ == 0 or _ == 3:
                self.color("GoldenRod")
            else:
                self.color("white")
            while self.xcor() < 600:
                self.pendown()
                self.forward(20)
                self.penup()
                self.forward(20)
            Y_COR += 180
