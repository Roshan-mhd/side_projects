from turtle import Turtle, Screen
from flat import Flat
from ball import Ball
from score import Score
import time

sc=Screen()
sc.setup(800,600)
sc.bgcolor("black")
sc.tracer(0)


l_flat = Flat((-350,0))
r_flat = Flat((350,0))
ball=Ball()
s=Score()
s.update_score()


sc.listen()
sc.onkey(r_flat.mov_flat_up,"Up")
sc.onkey(r_flat.mov_flat_down,"Down")
sc.onkey(l_flat.mov_flat_up,"w")
sc.onkey(l_flat.mov_flat_down,"s")


game_on=True

while game_on:
    sc.update()
    ball.move()
    time.sleep(ball.move_speed)


    if ball.ycor()>280 or ball.ycor()<-280:
        print("wall collision")
        ball.bounce_routine_wall()


    if (ball.xcor() < 340 and ball.distance(r_flat) < 50) or \
   (ball.xcor() < -320 and ball.distance(l_flat) < 50):
        print("flat collision")
        ball.bounce_routine_flat()



    if ball.xcor()>380:
        print("ball out right")
        ball.ball_reset()
        s.l_score_counter()
        

    if ball.xcor()<-380:
        print("ball out left")
        ball.ball_reset()
        s.r_score_counter()

        

sc.exitonclick()