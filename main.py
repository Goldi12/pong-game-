# #
# # #MAIN.PY FOR PONG GAME
# #
# # from turtle import Turtle, Screen
# # from paddle import Paddle
# # from ball import  Ball
# #
# #
# # screen = Screen()
# # screen.tracer(0)
# # screen.bgcolor("black")
# # screen.setup(width=800, height=600)
# # screen.title("pong")
# # ball = Ball()
# #
# # r_paddle = Paddle((350, 0))
# # l_paddle = Paddle((-350, 0))
# #
# # screen.listen()
# # screen.onkey(r_paddle.go_up, "Up")
# # screen.onkey(r_paddle.go_down, "Down")
# # screen.onkey(l_paddle.go_up, "w")
# # screen.onkey(l_paddle.go_down, "s")
# #
# # game_on = True
# # while game_on:
# #     screen.update()
# #
# # screen.exitonclick()
# #
# # #PADDLY.PY FOR FOR PADDLES
# #
# #
# # # BALL CREATING
#
#
#
#
#
#
#
#
#
#
#
# # from paddle import Paddle
# # from turtle import Turtle, Screen
# # import time
# # screen = Screen()
# #
# # screen.setup(width=800, height=600)
# #
# # time.sleep(0.2)
# # r_paddle = Paddle((350, 0))
# # l_paddle = Paddle((-350, 0))
# #
# # screen.listen()
# # screen.onkey(r_paddle.go_up, "Up")
# # screen.onkey(r_paddle.go_down, "Down")
# #
# #
# #
# #
# #
# #
# # screen.exitonclick()
# from scoreboard import Scoreboard
# import time
#
# from ball import Ball
# from paddle import  Paddle
# from turtle import Turtle, Screen
# screen = Screen()
# screen.tracer(0)
# ball = Ball()
# scoreboard = Scoreboard()
#
# screen.setup(width=800, height=600)
# r_paddle = Paddle((350, 0))
# l_paddle = Paddle((-350, 0))
# screen.listen()
# screen.onkey(r_paddle.go_up, "Up")
# screen.onkey(r_paddle.go_down, "Down")
# screen.onkey(l_paddle.go_up, "w")
# screen.onkey(l_paddle.go_down, "s")
#
#
# game_on = True
# while game_on:
#     screen.update()
#     time.sleep(ball.move_speed)
#     ball.move()
#     if ball.ycor() > 280 or ball.ycor() < -280:
#         ball.bounce_y()
#
#     if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
#         ball.bounce_x()
#
#     if ball.xcor() > 380:
#         ball.reset_postion()
#         scoreboard.clear()
#         scoreboard.l_point()
#     if ball.xcor() < -380:
#         ball.reset_postion()
#         scoreboard.clear()
#         scoreboard.r_point()
#
# screen.exitonclick()
from scoreboard import  Scoreboard
from ball import Ball
from paddle import  Paddle
from turtle import  Screen
import  time
screen = Screen()
scoreboard = Scoreboard()
screen.tracer(0)
screen.setup(width=800, height= 600)
ball = Ball()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    if ball.ycor() >280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.xcor() > 350:
        scoreboard.l_point()
        ball.reset_position()
    if ball.xcor() < -350:
        scoreboard.r_point()
        ball.reset_position()


    if r_paddle.distance(ball) < 50 and r_paddle.xcor() > 280 or l_paddle.distance(ball) < 50 and l_paddle.xcor() < -280:
        ball.bounce_x()

screen.exitonclick()