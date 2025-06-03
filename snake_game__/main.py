from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score import Score


s = Screen()
s.title("The Snake Game")
s.bgcolor("white")
s.setup(width=600, height=600)
sc=Score()
fod=Food()
snak = Snake()


    
s.tracer(0)

snake_alive = True

while snake_alive:
    s.update()
    time.sleep(0.15)

    snak.move()


    s.listen()
    s.onkey(snak.left,"a")
    s.onkey(snak.right,"d")
    s.onkey(snak.up,"w")
    s.onkey(snak.down,"s")

    if snak.head.distance(fod) < 15:
        print("food collisiion")
        fod.food_cords()
        sc.score_up()
        snak.snake_grow()

    if snak.head.xcor() > 299 or snak.head.xcor() < -299 or snak.head.ycor() < -299 or snak.head.ycor() > 299:
        print("wall collision")
        snake_alive = False
        sc.game_over()


    for seg_cell in snak.segments:
        if seg_cell == snak.head:
            pass
        elif snak.head.distance(seg_cell)<2:
            snake_alive=False
            sc.game_over()

s.exitonclick()