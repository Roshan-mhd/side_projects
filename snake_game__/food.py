from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.75,0.75)
        self.penup()
        self.color("black")
        self.speed("fastest")
        self.food_cords()

    def food_cords(self):
        rand_x = random.randint(-290,290)
        rand_y = random.randint(-290,290)
        self.goto(rand_x,rand_y)