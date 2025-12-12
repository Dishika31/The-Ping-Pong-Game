#w=20,h=20,x,y=0,0 and on every refresh, ball moves up, right every time
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,0)
        self.color("white")
        self.shape("circle")
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1

    def move(self):
        x,y = self.xcor(), self.ycor()
        self.goto(x + self.xmove, y + self.ymove)
    def reset(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()

    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1
        self.move_speed *= 0.9

