import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.all_car:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect finishing line
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.increase_car_speed()
        scoreboard.up_level()


screen.exitonclick()
