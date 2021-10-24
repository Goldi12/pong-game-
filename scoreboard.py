# # from turtle import  Turtle
# #
# # class Scoreboard(Turtle):
# #     def __init__(self):
# #         super().__init__()
# #         self.color("red")
# #         self.penup()
# #         self.hideturtle()
# #         self.l_score = 0
# #         self.r_score = 0
# #         self.update_scoreboard()
# #     def update_scoreboard(self):
# #
# #         self.goto(-100, 200)
# #         self.write(self.l_score, align= "center", font=("courier", 80, "normal"))
# #         self.goto(100, 200)
# #         self.write(self.r_score, align= "center", font=("courier", 80, "normal"))
# #
# #     def l_point(self):
# #         self.l_score += 1
# #         self.update_scoreboard()
# #
# #     def r_point(self):
# #         self.r_score += 1
# #         self.update_scoreboard()
# #
#
#
#
#
#
#
# from turtle import Turtle
# class Scoreboard(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.color("red")
#         self.hideturtle()
#         self.penup()
#         self.l_score = 0
#         self.r_score = 0
#         self.update_score()
#
#
#
#     def update_score(self):
#         self.goto(-100, 200)
#         self.write(self.l_score, align="center", font= ("courier", 80, "normal"))
#         self.goto(100, 200)
#         self.write(self.r_score, align="center", font= ("courier", 80, "normal"))
#     def l_point(self):
#         self.l_score += 1
#         self.update_score()
#     def r_point(self):
#         self.r_score += 1
#         self.update_score()
#
#
#
#
#
#
#
#
from turtle import  Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("red")
        self.hideturtle()
        self.penup()
        self.update_score()


    def update_score(self):
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("courier", 50, "normal"))
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("courier", 50, "normal"))

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_score()
    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_score()