from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.goto(0, -40)


    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)


    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def recenter(self):
        self.y_move *= -1
        self.goto(0, -40)