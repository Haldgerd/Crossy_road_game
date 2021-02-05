from turtle import Screen
from time import sleep

from turtle_object_class import Frog
from screen_modification_class import BorderText
from level_up import Level
from driving_cars_class import Car

# ------------- GLOBAL VARIABLES -----------------
COLOR = "white"
SHAPES = ["./Images/cars/resize_library_van.gif"]


# ------------ SCREEN INITIALIZATION --------------
screen = Screen()
screen.register_shape("./Images/frog_resize_sharp_nobg.gif")
screen.setup(width=1200, height=900, starty=None, startx=None)
screen.title("Frog Crossing")
screen.bgcolor(COLOR)
screen.tracer(0)

# -------------- OBJECTS INITIALIZATION ----------------
# writes title on the middle of screen
greet = BorderText()
greet.title()

# -------------- GAME OVER TEXT ------------------
game_over = BorderText()

# draws a border
border = BorderText()
border.draw_border()

# creates a turtle object, sets shape, informs of current level
screen.register_shape("./Images/cars/resize_library_van.gif")
van = Car()
van.shape(".Images/cars/resize_library_van.gif")

frog = Frog()
frog.shape("./Images/frog_resize_sharp_nobg.gif")
level_text = Level()
sleep(2)
level_text.clear()

# --------------- EVENT LISTENERS ------------------
screen.listen()
screen.onkeypress(frog.move, "Up")

# ---------------- MAIN LOGIC ------------------
game_on = True
while game_on:
    van.move()
    screen.update()
    sleep(0.07)

# CHECK IF FROG CROSSED THE ROAD SUCCESSFULLY.
    if frog.ycor() > 420:
        frog.reset_frog()
        level_text.level_up()
        # TODO: add speed to cars but first clear them all and upon new level spawn them anew.

# TODO: CHECK FOR COLLISION
#     if self.distance(to any car object) < 50:
#         write game over
#         level_text.game_over()

screen.exitonclick()


