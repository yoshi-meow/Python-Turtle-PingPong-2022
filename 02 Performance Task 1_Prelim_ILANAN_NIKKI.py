
#02 Performance Task 1/Prelim - ARG
#ILANAN, NIKKI C.

import turtle
score_1 = 0
score_2 = 0

#THIS IS MY SCREEN
screen = turtle.Screen()
screen.title("Puss Ping Pong Pang") #THIS IS MY TITLE, NAME OF MY CATS (PUSS, PING2X, PONG2X, PANG2X) ^_^
screen.bgcolor("green")
screen.setup(width=800, height=600)
screen.tracer(0)

#THIS IS MY NET FOR PINGPONG TABLE
net = turtle.Turtle()
net.shape("square")
net.color("white")
net.shapesize(stretch_wid=25, stretch_len=1)


#THIS IS PLAYER 1 PADDLE
player_1 = turtle.Turtle()
player_1.speed(0)
player_1.shape("square")
player_1.color("darkturquoise")
player_1.shapesize(stretch_wid=5, stretch_len=1)
player_1.penup()
player_1.goto(-350, 0)

#THIS IS PLAYER 2 PADDLE
player_2 = turtle.Turtle()
player_2.speed(0)
player_2.shape("square")
player_2.color("firebrick1")
player_2.shapesize(stretch_wid=5, stretch_len=1)
player_2.penup()
player_2.goto(350, 0)

#THIS IS THE PINGPONG BALL
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("orange1")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1

#THIS IS FOR THE SCORE BOARD
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 20, "bold"))

def player_1_up():
    y = player_1.ycor()
    y += 30
    player_1.sety(y)
def player_1_down():
    y = player_1.ycor()
    y -= 30
    player_1.sety(y)
def player_2_up():
    y = player_2.ycor()
    y += 30
    player_2.sety(y)
def player_2_down():
    y = player_2.ycor()
    y -= 30
    player_2.sety(y)

    
#THIS IS FOR THE CONTROLS OF PLAYER 1 AND PLAYER 2
screen.listen()
screen.onkeypress(player_1_up, "w")
screen.onkeypress(player_1_down, "s")
screen.onkeypress(player_2_up, "Up")
screen.onkeypress(player_2_down, "Down")
while True:
    screen.update()

    #BALL MOVE
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #BORDER CHECK
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    #LEFT AND RIGHT
    if (ball.xcor() < -340 and ball.xcor() > -350) and (player_1.ycor() + 50 > ball.ycor() > player_1.ycor() - 50):
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 20, "bold"))
    if ball.xcor() > 380:
        score_1 = 0
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 20, "bold"))
        ball.goto(0, 0)
        ball.dx *= -1


    if (ball.xcor() > 340 and ball.xcor() < 350) and (player_2.ycor() + 50 > ball.ycor() > player_2.ycor() - 50):
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 20, "bold"))
    if ball.xcor() < -380:
        score_2 = 0
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 20, "bold"))
        ball.goto(0, 0)
        ball.dx *= -1


    #THIS IS PADDLE AND BALL COLLISIONS
    if (ball.xcor() > 340 and ball.xcor() < 350) and (player_2.ycor() + 50 > ball.ycor() > player_2.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (player_1.ycor() + 50 > ball.ycor() > player_1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
