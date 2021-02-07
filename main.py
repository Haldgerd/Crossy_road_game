from turtle import Screen
from time import sleep
from random import choice, randint

from turtle_object_class import Dog
from screen_modification_class import BorderTextRoad
from level_up import Level
from driving_cars_class import Car

# ------------- GLOBAL VARIABLES & VARIABLES -----------------
COLOR = "grey"
SHAPES = ["./Images/bus.gif", "./Images/caravan-car.gif", "./Images/blue-car.gif", "./Images/bear_bike.gif",
          "./Images/big_bus.gif", "./Images/mechanic_car.gif", "./Images/taxi_car.gif", "./Images/two_cars.gif"]

# ------------ SCREEN INITIALIZATION --------------
screen = Screen()
screen.register_shape("./Images/dog.gif")
screen.setup(width=1200, height=900, starty=None, startx=None)
screen.title("Frog Crossing")
screen.bgcolor(COLOR)
screen.tracer(0)

# creates a turtle object, registers shapes, informs player of current level
for shape in range(len(SHAPES)):
    screen.register_shape(SHAPES[shape])

# -------------- OBJECTS INITIALIZATION ----------------
# writes title on the middle of screen
greet = BorderTextRoad()
greet.title()

# -------------- GAME OVER TEXT ------------------
game_over = BorderTextRoad()

# draws a border on each side of the screen
border = BorderTextRoad()
border.draw_border()

# draws a road marking
roads = BorderTextRoad()
roads.draw_road()

dog = Dog()
dog.shape("./Images/dog.gif")

car_manager = Car()

level_text = Level()
sleep(2)
level_text.clear()

# --------------- EVENT LISTENERS ------------------
screen.listen()
screen.onkeypress(dog.move, "Up")
# screen.onkeypress(dog.move_right, "Right") This part of code didn't work.
# I suspect it's the custom shape of the object that is preventing it from working properly.

# ---------------- MAIN LOGIC ------------------
loop_count = 1
game_on = True
while game_on:
    screen.update()
    sleep(0.06)

# create a car object every 6th time a loop runs.
    if loop_count % 6 == 0:
        car_manager.create_car()

# move cars along y axis
    car_manager.move_car()

# CHECK IF FROG CROSSED THE ROAD SUCCESSFULLY.
    if dog.ycor() > 400:
        dog.reset_player()
        level_text.level_up()
        car_manager.reset_car()

# CHECK FOR COLLISION with any car object.
    for car in car_manager.all_cars:
        if car.distance(dog) < 40:
            level_text.game_over()
            game_on = False

    loop_count += 1

screen.exitonclick()


