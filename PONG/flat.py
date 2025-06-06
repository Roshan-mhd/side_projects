from turtle import Turtle


class Flat(Turtle):
    def __init__(self,pos_tuple):
        super().__init__()
        self.shape("square")
        self.color("White")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(pos_tuple)


    def mov_flat_up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(),new_y)

    def mov_flat_down(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(),new_y)