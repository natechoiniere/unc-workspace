# Enemy and Player
import turtle
import os


# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders!")


# Draw border
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


# Create player turtle
player = turtle.Turtle()
player.speed(0)
player.setheading(90)
player.color("blue")
player.shape("triangle")
player.penup()
player.setposition(0, -250)
playerspeed = 15



# Create the enemy
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)
enemyspeed = 2

# Move the player left and right
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


# Player fires bullet with spacebar
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
bulletspeed = 20


# Define bullet states (ready, ready to fire; firing, bullet is firing)
bulletstate = "ready"

def fire_bullet():
    # Declare bulletstate as a global if it needs to be changed
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        bullet.showturtle()
        x = player.xcor()
        y = player.ycor()
        bullet.setposition(x, y + 10)
        

# Create keyboard bindings
turtle.listen()
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")
turtle.onkeypress(move_up, "Up")
turtle.onkeypress(move_down, "Down")
turtle.onkeypress(fire_bullet, "space")


# Main game loop
while True:

    # Move the enemy
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    # Prevent enemies from going past walls
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

    # Moving the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    # Prevent bullet from passing the top wall
    if bullet.ycor() > 280:
        bullet.hideturtle()
        bulletstate = "ready"
        
delay = input("Press enter to finish.")