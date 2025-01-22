from turtle import Screen
from paddle import Paddle
from ball import Ball
from middle_line import MiddleLine
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


left_paddle = Paddle(x_pos=-365, y_pos=0)
right_paddle = Paddle(x_pos=350, y_pos=0)
ball = Ball()
scoreboard = Scoreboard()
middle_line = MiddleLine()


screen.listen()
# Left Paddle
screen.onkeypress(key="w", fun=left_paddle.go_up)
screen.onkeypress(key="s", fun=left_paddle.go_down)
# Right Paddle
screen.onkeypress(key="Up", fun=right_paddle.go_up)
screen.onkeypress(key="Down", fun=right_paddle.go_down)


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detected Collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detected Collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 325 or ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()


    # Detect if the ball goes beyond the screen limit and restart the game
    ## Right paddle miss:
    if ball.xcor() > 400:
        ball.reset_position()
        time.sleep(1)
        scoreboard.left_point()

    ## Left paddle miss:
    if ball.xcor() < -400:
        ball.reset_position()
        time.sleep(1)
        scoreboard.right_point()



screen.exitonclick()
