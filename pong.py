import turtle as t
import os

playerAscore = 0
playerBscore = 0

window = t.Screen()
window.title("Ping Pong Game")
window.bgcolor('black')
window.setup(width=1000, height=800)
window.tracer(0)

# creating left paddle
leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350, 0)

# creating right paddle
rightpaddle = t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350, 0)

# creating ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ballxdirection = 1.5
ballydirection = 1.5

# creating pen for updating scorecard
pen = t.Turtle()
pen.speed(0)
pen.color('skyblue')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("score", align="center", font=('Arial', 24, 'normal'))

# moving leftpaddle


def leftpaddleup():
    y = leftpaddle.ycor()
    y = y + 15
    leftpaddle.sety(y)


def leftpaddledown():
    y = leftpaddle.ycor()
    y = y - 15
    leftpaddle.sety(y)

# moving rightpaddle


def rightpaddleup():
    y = rightpaddle.ycor()
    y = y + 15
    rightpaddle.sety(y)


def rightpaddledown():
    y = rightpaddle.ycor()
    y = y - 15
    rightpaddle.sety(y)


# assign keys to play the Game
window.listen()
window.onkeypress(leftpaddleup, 'w')
window.onkeypress(leftpaddledown, 's')
window.onkeypress(rightpaddleup, 'i')
window.onkeypress(rightpaddledown, 'k')

while True:
    window.update()

    # moving the ball
    ball.setx(ball.xcor() + ballxdirection)
    ball.sety(ball.ycor() + ballydirection)

    # setting up border
    if ball.ycor() > 290:
        ball.sety(290)
        ballydirection = ballydirection * -1

    if ball.xcor() > -290:
        ball.setx(-290)
        ballxdirection = ballxdirection * -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ballxdirection = ballxdirection
        playerAscore = playerAscore + 1
        os.system("afplay wallhit.wav&")
        pen.clear()
        pen.write("Player A :{}    Player B :{}".format(playerAscore,
                  playerBscore), align="center", font=('Arial', 24, 'normal'))

    # handling the collissions
    # if (ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < rightpaddle.ycor() + 40 and ball.ycor() > rightpaddle.ycor() - 40):
    #     ball.setx(340)
    #     ballxdirection = ballxdirection * -1
    #     os.system("afplay paddle.wav&")
    # if (ball.xcor() < 340) and (ball.xcor() > 350) and (ball.ycor() < leftpaddle.ycor() + 40 and ball.ycor() > leftpaddle.ycor() - 40):
    #     ball.setx(-340)
    #     ballxdirection = ballxdirection * -1
    #     os.system("afplay paddle.wav&")

    if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < rightpaddle.ycor() + 40 and ball.ycor() > rightpaddle.ycor() - 40):
        ball.setx(340)
        ballxdirection = ballxdirection * -1
        os.system("afplay paddle.wav&")

    if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < leftpaddle.ycor() + 40 and ball.ycor() > leftpaddle.ycor() - 40):
        ball.setx(-340)
        ballxdirection = ballxdirection * -1
        os.system("afplay paddle.wav&")
