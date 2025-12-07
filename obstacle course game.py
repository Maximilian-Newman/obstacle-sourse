try:
    file = open("obstacle course high score.mrt", "r")
    highScore = int(file.read())
    file.close()
except:
    highScore = 0
    file = open("obstacle course high score.mrt", "w")
    file.write(str(0))
    file.close()


import turtle
import time
import random

turtle.hideturtle()
turtle.speed(0)
turtle.width(10)


player = turtle.Turtle()
player.speed(3)
player.penup()
player.shape("turtle")
player.color("green")

obstacle1 = turtle.Turtle()
obstacle1.penup()
obstacle1.speed(0)
obstacle1.shape("square")
obstacle1.color("red")


obstacle2 = turtle.Turtle()
obstacle2.penup()
obstacle2.speed(0)
obstacle2.shape("square")
obstacle2.color("red")


obstacle3 = turtle.Turtle()
obstacle3.penup()
obstacle3.speed(0)
obstacle3.shape("square")
obstacle3.color("red")



scoreD = turtle.Turtle()
scoreD.hideturtle()
scoreD.speed(0)
scoreD.penup()
scoreD.goto(290, 40)

score = 0
playerY = 0

def delay(secs):
    secs += time.time()
    while secs > time.time():
        doNothing = "ghjfkjsk"
        turtle.forward(0)

def jump():
    global playerY
    global lastJump
    
    if playerY == 0:
        playerY = 40
        lastJump = time.time()

def showScore():
    global score
    global highScore
    scoreD.clear()
    if highScore > score:
        scoreD.color("blue")
        scoreD.write("score: " + str(score) + "  -  High-score: " + str(highScore), align="right", font=(None, 15, "bold"))
    else:
        scoreD.color("green")
        scoreD.write("NEW HIGH SCORE!: " + str(score), align="right", font=(None, 15, "bold"))



playing = False

def setupGame():
    global playing
    global obstacle1X
    global obstacle2X
    global obstacle3X
    global obs1speed
    global obs2speed
    global obs3speed
    global nextObst1
    global nextObst2
    global nextObst3
    global playerY
    global lastJump
    global score
    global startTime

    turtle.clear()
    turtle.penup()
    turtle.goto(0, -40)
    turtle.write("press space to jump", align="center", font=(None, 20, "bold"))
    turtle.goto(-300, 0)
    turtle.pendown()
    turtle.goto(300, 0)

    obstacle1X = 300
    obstacle2X = 300
    obstacle3X = 300
    obs1speed = random.randint(6, 8)
    obs2speed = random.randint(6, 8)
    obs3speed = random.randint(6, 8)
    nextObst1 = time.time() + 3
    nextObst2 = time.time() + 5
    nextObst3 = time.time() + 7
    playerY = 0
    lastJump = 0
    score = 0
    showScore()
    startTime = time.time()
    playing = True

setupGame()

def r_pressed():
    global playing
    if playing == False:
        setupGame()

screen = turtle.Screen()
screen.listen()
screen.onkey(jump, 'space')
screen.onkey(jump, 'Up')
screen.onkey(r_pressed, 'r')

while True:
    turtle.forward(0)
    
    while playing:
        player.goto(0, playerY + 15)
        obstacle1.goto(obstacle1X, 15)
        obstacle2.goto(obstacle2X, 15)
        obstacle3.goto(obstacle3X, 15)

        if lastJump < time.time() - 1:
            playerY = 0


        if nextObst1 < time.time():
            obstacle1X = obstacle1X - obs1speed

        if nextObst2 < time.time():
            obstacle2X = obstacle2X - obs2speed

        if nextObst3 < time.time():
            obstacle3X = obstacle3X - obs3speed


        if obstacle1X < -200:
            score += obs1speed
            obstacle1.goto(300, 15)
            obs1speed = random.randint(6, 8 + int(score/20))
            nextObst1 = time.time() + random.randint(0, 5)
            obstacle1X = 300
            showScore()
        
        if obstacle2X < -200:
            score += obs2speed
            obstacle2.goto(300, 15)
            obs2speed = random.randint(6, 8 + int(score/20))
            nextObst2 = time.time() + random.randint(0, 5)
            obstacle2X = 300
            showScore()
        
        if obstacle3X < -200:
            score += obs3speed
            obstacle3.goto(300, 15)
            obs3speed = random.randint(6, 8 + int(score/20))
            nextObst3 = time.time() + random.randint(0, 5)
            obstacle3X = 300
            showScore()
        

        if obstacle1X < 20 and obstacle1X > -20 and playerY < 12:
            player.goto(0, 15)
            playing = False
            turtle.penup()
            turtle.goto(0, 100)
            turtle.write("Game Over", align="center", font=(None, 50, "bold"))
            turtle.goto(0, 70)
            turtle.write("press R to restart", align="center", font=(None, 20, "bold"))
            if score > highScore:
                highScore = score
                file = open("obstacle course high score.mrt", "w")
                file.write(str(score))
                file.close()

        if obstacle2X < 20 and obstacle2X > -20 and playerY < 12:
            player.goto(0, 15)
            playing = False
            turtle.penup()
            turtle.goto(0, 100)
            turtle.write("Game Over", align="center", font=(None, 50, "bold"))
            turtle.goto(0, 70)
            turtle.write("press R to restart", align="center", font=(None, 20, "bold"))
            if score > highScore:
                highScore = score
                file = open("obstacle course high score.mrt", "w")
                file.write(str(score))
                file.close()

        if obstacle3X < 20 and obstacle3X > -20 and playerY < 12:
            player.goto(0, 15)
            playing = False
            turtle.penup()
            turtle.goto(0, 100)
            turtle.write("Game Over", align="center", font=(None, 50, "bold"))
            turtle.goto(0, 70)
            turtle.write("press R to restart", align="center", font=(None, 20, "bold"))
            if score > highScore:
                highScore = score
                file = open("obstacle course high score.mrt", "w")
                file.write(str(score))
                file.close()

