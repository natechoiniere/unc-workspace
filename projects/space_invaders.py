#Space Invaders - Part 3
#Set up the screen
import turtle
import os

#Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders!")

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Create player turtle
player = turtle.Turtle()
player.speed(0)
player.setheading(90)
player.color("blue")
player.shape("triangle")
player.penup()
player.setposition(0, -250)

playerspeed = 15
enemyspeed = 2

#Create the enemy
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

#Move the player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)
def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)
def move_up():
    y = player.ycor()
    y += playerspeed
    if y > 280:
        y = 280
    player.sety(y)
def move_down():
    y = player.ycor()
    y -= playerspeed
    if y < -280:
        y = -280
    player.sety(y)

#Create keyboard bindings
turtle.listen()
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")
turtle.onkeypress(move_up, "Up")
turtle.onkeypress(move_down, "Down")

#Main game loop
while True:

    #Move the enemy
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    #Prevent enemies from going past walls
    if enemy.xcor() > 280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)

    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)

delay = input("Press enter to finish.")