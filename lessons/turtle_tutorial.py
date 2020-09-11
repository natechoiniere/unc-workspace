"""Turtle tutorial."""


__author__ = "730443739"

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
bob: Turtle = Turtle()
side_length: int = 300

leo.hideturtle()
colormode(255)
leo.speed(50)
leo.pencolor(123, 197, 242)
leo.fillcolor(123, 197, 242)
leo.penup()
leo.goto(-150, 0)
leo.pendown()

# bob.hideturtle()
bob.penup()
bob.speed(100)
bob.goto(-150,0)
bob.pendown()
bob.pencolor(0, 0, 0)
bob.fillcolor(0, 0, 0)

i: int = 0
leo.begin_fill()
while (i < 3):
    
    leo.forward(side_length)
    leo.left(120)
    
    i = i + 1
leo.end_fill()

i = 0
while (i < 3):
    
    bob.forward(side_length)
    bob.left(120)
    
    i = i + 1

i = 0
while (i < 100):
    side_length = side_length * 0.97
    bob.forward(side_length)
    bob.left(122)
    i = i + 1
done()