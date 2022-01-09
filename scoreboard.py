from turtle import Turtle
FONT = ("Courier", 30, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score_writer = Turtle()
        self.score_writer.hideturtle()
        self.score_writer.penup()
        self.hearts_writer = Turtle()
        self.hearts_writer.penup()
        self.hearts_writer.hideturtle()
        self.score = 0
        self.hearts = 4
        self.update_score()
        self.update_hearts()


    def update_score(self):
        self.score_writer.goto(300, 250)
        self.score_writer.clear()
        self.score_writer.write(f"Score: {self.score}", align="center", font=FONT)


    def update_hearts(self):
        self.hearts_writer.goto(-300, 250)
        self.hearts_writer.clear()
        self.hearts_writer.write(f"Hearts: {self.hearts}", align="center", font=FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over\nScore: {self.score}", align="center", font=("Courier", 50, "normal"))


