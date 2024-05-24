import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.move_speed = MOVE_INCREMENT


    def make_car(self):
        car = Turtle('square')
        car.color(random.choice(COLORS))
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.goto(310, random.randint(-250,250))
        self.cars.append(car)

    def move_left(self):
        for car in self.cars:
            new_x = car.xcor() - self.move_speed
            car.goto(new_x, car.ycor())


    def update_speed(self):
        self.move_speed += 5
