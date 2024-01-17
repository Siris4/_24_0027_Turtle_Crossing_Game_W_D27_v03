
from turtle import Turtle, Screen


#turtle movement (it can only move forwards, not back, left or right)
#When the turtle hits the top edge of the screen, it moves back to the original position and the player levels up. On the next level, the car speed increases.
#When the turtle collides with a car, it's game over and everything stops.

#CONSTANTS:
TURTLE_STARTING_POSITION = (0, -280)
TURTLE_MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# screen = Screen()    #don't need this here. don't need this if it's not the Main.py file

# TODO 1: Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north: Done.


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.go_to_starting_line()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        # self.turtle_movement_distance = TURTLE_MOVE_DISTANCE   #this is redundant. this needs to get it's own Method (shown below). It's a function. Not an Attribute.

    def turtle_move_upwards(self):
        self.forward(TURTLE_MOVE_DISTANCE)  # this code is to manually move it forward.
           #to AUTO-move, well you need this code instead:
        # new_x = self.xcor() + self.x_move
        # new_y = self.ycor() + self.y_move
        # self.goto(new_x, new_y)

    # TODO 4: Detect when turtle reaches the other side: y=280

    # Detect successful Finish Line:
    # if player.pos() > FINISH_LINE_Y:
    #     print("You leveled up!!!")

    def go_to_starting_line(self):
        self.goto(TURTLE_STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

# player = Player()      #don't need this here either. don't need this if it's not the Main.py file

# screen.exitonclick()    #you can remove this too. don't need this if it's not the Main.py file