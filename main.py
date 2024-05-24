import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
player = Player()
screen.onkeypress(player.move_up, "Up")
car_manager = CarManager()
scoreboard = Scoreboard()
loop_count = 1

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_left()
    if loop_count > 5:
        car_manager.make_car()
        loop_count = 0

    loop_count += 1
    for car in car_manager.cars:
        if car.ycor() - 20 < player.ycor() < car.ycor() + 20:
            if player.distance(car) < 30:
                scoreboard.game_over()
                game_is_on = False

    if player.ycor() > 290:
        player.go_to_start()
        car_manager.update_speed()
        scoreboard.add_level()

screen.exitonclick()
