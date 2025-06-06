from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.speed("normal")
        self.x_move_pace = 10
        self.y_move_pace = 10
        self.move_speed=0.1

    def move(self):
        new_x=self.xcor()+self.x_move_pace
        new_y = self.ycor()+self.y_move_pace
        self.goto(new_x,new_y)

    def bounce_routine_wall(self):
        self.y_move_pace *= -1 

    def bounce_routine_flat(self):
        self.x_move_pace*=-1
        self.move_speed*=0.9

    def ball_reset(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.bounce_routine_flat()