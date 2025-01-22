from turtle import Turtle

class MiddleLine(Turtle):
    def __init__(self):
        super().__init__()
        self.color("gray")
        self.penup()
        self.draw_line()


    def draw_line(self):
        self.pensize(3)
        self.goto(x=0, y=-280)
        self.setheading(-270)

        for i in range(30):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
