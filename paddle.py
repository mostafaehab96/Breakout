from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_len=5)
        self.penup()
        self.goto(0, -260)


    def move_right(self):
        self.setx(self.xcor() + 20)

    def move_left(self):
        self.setx(self.xcor() - 20)