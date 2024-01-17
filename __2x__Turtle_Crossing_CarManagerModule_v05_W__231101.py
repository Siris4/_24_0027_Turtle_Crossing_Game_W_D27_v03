import time
from turtle import Turtle
import random

#car flow, speed, size, color,
#cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.



CAR_COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
CAR_STARTING_MOVE_DISTANCE = 5
CAR_MOVE_INCREMENT_AFTER_LEVEL_UP = 10   #Car move distance increases by 10 every time the Player levels up from completing each individual stage
# CAR_Y_RANGE = (320, -240) to (320, 240)   #this gets placed into the def create_cars block, below


# TODO 2: Create Car Class and move the cars: Done.

#carmanager:
class CarManager(Turtle):
    def __init__(self):
        super().__init__()

    def __init__(self):
        self.all_cars = []   #because we are defining this within a Class, self. MUST be in front!
        self.car_speed = CAR_STARTING_MOVE_DISTANCE  #(for above): and NOW you can type self.all_cars.append(new_car) below - new_car gets appended.

    def create_car(self):
        # time.sleep(1.0)   #so instead of placing this here, and slowing the WHOLE annimation down, you could use this:
        car_generated_chance = random.randint(1, 6)  #you create a random CHANCE that a car MIGHT be populated every 0.1 seconds to stagger it way more sporatically.
        if car_generated_chance == 1:
            new_car = Turtle("square")
            # new_car.shape("square")   #the line above replaces this line, as well as adding new_car
            new_car.penup()
            new_car.color(random.choice(CAR_COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # higher number for length makes it a horizontal looking Object!
        # (0, -280) is the starting turtle location, ending is +280. Cars will go as low as -240, and as high as 240.
        # x should start at +320, and the y will be random choice
            y_range_for_cars = random.randint(-240, 240)
            new_car.goto(300, y_range_for_cars)
            self.all_cars.append(new_car)

    def level_up(self):
        self.car_speed += CAR_MOVE_INCREMENT_AFTER_LEVEL_UP

    def car_movement(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
        # self.x_move = CAR_STARTING_MOVE_DISTANCE
        # new_x = self.xcor() + self.
        # new_y = self.ycor() + self.y_move
        # self.goto(new_x, new_y)

#create Car
# class Car(Turtle):
#
#     def __init__(self):
#         super().__init__()
#         self.penup()
#         self.shape("square")
#         self.color(random.choice(CAR_COLORS))
#         self.shapesize(stretch_wid=1, stretch_len=2)   #higher number for length makes it a horizontal looking Object!
        # (0, -280) is the starting turtle location, ending is +280. Cars will go as low as -240, and as high as 240.
        # x should start at +320, and the y will be random choice
        # self.goto(270, 0)




