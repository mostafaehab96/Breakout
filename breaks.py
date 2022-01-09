from turtle import Turtle
from random import randint, choice

LINES = 5
LENGTHS = [3, 4, 5]
WIDTH = 1.8
START_Y = 220
START_X = -350

class Break(Turtle):
    def __init__(self):
        super().__init__()
        self.color(randint(0, 255), randint(0, 255), randint(0, 255))
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=WIDTH, stretch_len=choice(LENGTHS))
        self.goto(START_X, START_Y)


class Breaks():
    def __init__(self):
        self.breaks = []
        self.add_breaks()


    def add_breaks(self):
        for line in range(LINES):
            break_line = []
            first_break = Break()
            first_break.sety(START_Y - (line* 45))
            break_line.append(first_break)
            break_count = 0
            while True:
                new_break = Break()
                previous_break = break_line[break_count]
                width = max(previous_break.shapesize()[1], new_break.shapesize()[1])
                new_break.goto(previous_break.xcor() + (width * 21), START_Y - (line * 45))
                if new_break.xcor() >= 370:
                    new_break.hideturtle()
                    break
                break_count += 1
                break_line.append(new_break)
            self.breaks.append(break_line)




