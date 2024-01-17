#highest level so far: Level 8

import time

from turtle import Screen
from __2x__Turtle_Crossing_TurtlePlayerModule_v05_W__231101 import Player, FINISH_LINE_Y
from __2x__Turtle_Crossing_CarManagerModule_v05_W__231101 import CarManager
from __2x__Turtle_Crossing_ScoreboardModule_v03_W__231101 import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()   #SCREEN LISTENING AND ONKEY FUCNTIONS SHOULD ALWAYS BE BEFORE THE WHILE LOOP!
screen.onkey(fun=player.turtle_move_upwards, key="Up")


# if y >= FINISH_LINE_Y,
# then level_at_currently += 1

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    #whatever you place inside the while loop will be refreshed every 0.1 seconds.
    car_manager.create_car()
    car_manager.car_movement()

    # TODO 3: Detect Collision with car
    for car in car_manager.all_cars:   #get ahold of all_cars Object
        if car.distance(player) < 20: #if the car distance to the player (turtle object is 20 pixels)
            game_on = False
            scoreboard.game_over()
            screen.update()

    # TODO: once leveled up... increase by CAR_MOVE_INCREMENT
    if player.is_at_finish_line() == True:
        player.go_to_starting_line()
        car_manager.level_up()
        scoreboard.level += 1


        scoreboard.update_scoreboard()

    # if level < 0:

    # elif level >= 1:
    # self.x_move = CAR_MOVE_INCREMENT_AFTER_LEVEL_UP

    # elif level >= 2:
    # CAR_MOVE_INCREMENT_AFTER_LEVEL_UP += CAR_MOVE_INCREMENT_AFTER_LEVEL_UP

    # def car_movement_forward(self):
    # new_.forward(CAR_STARTING_MOVE_DISTANCE)


screen.exitonclick()