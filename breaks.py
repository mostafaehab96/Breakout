from turtle import Turtle
from random import randint, choice

LINES = 5
LENGTHS = [3, 4]
WIDTH = 1.8


class Break(Turtle):
    def __init__(self):
        super().__init__()
        self.color(randint(0, 255), randint(0, 255), randint(0, 255))
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=WIDTH, stretch_len=choice(LENGTHS))
        self.goto(-350, 270)


class Breaks():
    def __init__(self):
        self.breaks = []
        self.add_breaks()


    def add_breaks(self):
        for line in range(LINES):
            break_line = []
            first_break = Break()
            first_break.sety(270 - (line* 45))
            break_line.append(first_break)
            break_count = 0
            while True:
                new_break = Break()
                previous_break = break_line[break_count]
                new_break.goto(previous_break.xcor() + (previous_break.shapesize()[1] * 23), 270 - (line * 45))
                if new_break.xcor() >= 370:
                    new_break.hideturtle()
                    break
                break_count += 1
                break_line.append(new_break)
            self.breaks.append(break_line)




