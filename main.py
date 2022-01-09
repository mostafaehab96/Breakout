import turtle
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from breaks import Breaks
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Breakout Game")
turtle.tracer(0)
screen.listen()
turtle.colormode(255)

paddle = Paddle()
ball = Ball()
breaks = Breaks()
scoreboard = Scoreboard()

screen.onkey(key="Left", fun=paddle.move_left)
screen.onkey(key="Right", fun=paddle.move_right)

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0.05)

    if len(breaks.breaks) == 0:
        game_is_on = False
        scoreboard.game_over()

    # hitting the paddle
    if ball.distance(paddle) <= 60 and ball.ycor() < -230:
        ball.bounce_y()

    # hitting the top wall
    if ball.ycor() >= 270:
        ball.bounce_y()

    # hitting the bottom wall:
    if ball.ycor() < -270:
        time.sleep(1)
        ball.recenter()
        scoreboard.hearts -= 1
        scoreboard.update_hearts()
        if scoreboard.hearts == 0:
            game_is_on = False
            scoreboard.game_over()

    # hitting the right and left wall
    if abs(ball.xcor()) >= 370:
        ball.bounce_x()

    for break_line in breaks.breaks:
        for brek in break_line:
            distance = brek.shapesize()[1] * 11
            if ball.distance(brek) < distance:
                ball.bounce_y()
                break_line.remove(brek)
                brek.hideturtle()
                scoreboard.score += (scoreboard.hearts * 1)
                scoreboard.update_score()
        if len(break_line) == 0:
            breaks.breaks.remove(break_line)

turtle.mainloop()
