from turtle import Turtle
from random import choice

# y position of cars will be randomized in between the viable area so between -350 and 350.
X_POSITION = 700
POSSIBLE_Y_POSITIONS = [num for num in range(-250, 250, 80)]
MOVING_DISTANCE = 10
STARTING_MOVE_DISTANCE = 10
SHAPES = ["./Images/bus.gif", "./Images/caravan-car.gif", "./Images/blue-car.gif", "./Images/bear_bike.gif",
          "./Images/big_bus.gif", "./Images/mechanic_car.gif", "./Images/taxi_car.gif", "./Images/two_cars.gif"]


class Car:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        car = Turtle()
        car.shape(choice(SHAPES))
        car.penup()
        car.goto(x=X_POSITION, y=choice(POSSIBLE_Y_POSITIONS))
        car.setheading(180)
        self.all_cars.append(car)

    def move_car(self):
        for car in self.all_cars:
            if car.distance(self.all_cars[-1]) > 90:
                car.fd(MOVING_DISTANCE)

    def reset_car(self):
        self.car_speed += MOVING_DISTANCE
