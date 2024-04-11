import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
scoreboard = Scoreboard()
car_all = CarManager()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(player.move,"Up")

game_is_on = True
while game_is_on:
    
    time.sleep(0.1)
    screen.update()
    car_all.create_cars()
    car_all.move()
    
    for car in car_all.all_cars:

        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

        if player.finish_line():
            car_all.move_increase()
            scoreboard.increase_level()


screen.exitonclick()