# Pong Game
import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

WIDTH = 800
HEIGHT = 600

LEFT_PADDLE_STARTING_POS = -350
RIGHT_PADDLE_STARTING_POS = 350

# create screen
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

screen.listen()

# create two paddles
l_paddle = Paddle(LEFT_PADDLE_STARTING_POS)
r_paddle = Paddle(RIGHT_PADDLE_STARTING_POS)

screen.onkeypress(l_paddle.up, "a")
screen.onkeypress(l_paddle.down, "q")

screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

# create scoreboard
scoreboard = Scoreboard()
scoreboard.draw_net(WIDTH, HEIGHT)

ball = Ball()

game_is_on = True
while game_is_on:
    new_ball = False
    ball.setposition(0, 0)

    while not new_ball:
        screen.update()
        ball.move()
        time.sleep(ball.ball_speed)

        # detect collision with the wall and bounce
        y_pos = ball.ycor()
        x_pos = ball.xcor()
        if y_pos < -290 or y_pos > 290:
            ball.bounce_y()

        # detect collision with paddle
        if ball.distance(l_paddle) < 50 and ball.xcor() < -330 or ball.distance(r_paddle) < 50 and ball.xcor() > 330:
            ball.bounce_x()

        # detect when paddle misses
        if x_pos > 390:
            ball.reset_position()
            game_is_on = scoreboard.increase_score(x_pos)
            scoreboard.update_scoreboard()
            new_ball = True

        if ball.xcor() < -390:
            ball.reset_position()
            game_is_on = scoreboard.increase_score(x_pos)
            scoreboard.update_scoreboard()
            new_ball = True

    scoreboard.draw_net(WIDTH, HEIGHT)

screen.exitonclick()
