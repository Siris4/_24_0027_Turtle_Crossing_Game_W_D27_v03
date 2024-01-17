
from turtle import Turtle

#handles the scoreboard and the Game Over sequence.

FONT = ("Courier", 24, "normal")

# TODO 5: Create a Scoreboard and the Game Over sequence:

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        # self.score = 0
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-250, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("black")
        self.write(f"GAME OVER BRAH", align="center", font=FONT)
