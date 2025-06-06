from turtle import Turtle



class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-245,278)
        self.write(f"Score is: {self.score}",align = "center", font = ("Arial", 15, "normal"))

    def score_up(self):
        self.score=self.score+1
        self.clear()
        self.write(f"Score is: {self.score}",align = "center", font = ("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!!", align = "center", font = ("Arial",30,"normal"))