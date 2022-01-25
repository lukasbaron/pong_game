from turtle import Turtle

BALL_SPEED = 3

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1, 1)
        self.color("white")
        self.penup()
        self.setx(0)
        self.sety(0)
        self.x_move = BALL_SPEED
        self.y_move = BALL_SPEED
        self.xcor()

    def movement(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        self.bounce_y()

    def bounce_x(self):
             self.x_move = self.x_move * - 1

    def bounce_y(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_move = self.y_move * - 1



