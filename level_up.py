from turtle import Turtle
from time import sleep

FONT = "Courier New"
COLOR = "SeaGreen"


class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=0)
        self.color(COLOR)
        self.level = 1
        self.write(f"Level: {self.level}", align="center", font=(FONT, 40, "normal"))

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=(FONT, 40, "normal"))
        sleep(2)
        self.clear()

    def game_over(self):
        self.write("GAME OVER", align="center", font=(FONT, 50, "bold"))