from turtle import Turtle
#move up = 20 px

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.shape("square")
        self.color("white")
        self.shapesize(5 ,1)
    def up(self):
        x = self.position()[0]
        y = self.position()[1]
        self.goto(x,y + 10)
    def down(self):
        x = self.position()[0]
        y = self.position()[1]

        self.goto(x, y - 10)


