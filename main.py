import time
from turtle import Screen, Turtle

import paddle
from ball import Ball
from paddle import Paddle


screen = Screen()
ball = Ball()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong game")
screen.delay()

screen.listen()

screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

score_left_paddle = 0
score_right_paddle = 0

game_is_on = True

while game_is_on:
    screen.update()
    ball.movement()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_x()
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    if ball.xcor() > 420:
        score_left_paddle += 1
        print(score_left_paddle)
        ball.setx(0)
        ball.sety(0)

    elif ball.xcor() < -420:
        score_right_paddle += 1
        print(score_right_paddle)
        ball.setx(0)
        ball.sety(0)





screen.exitonclick()