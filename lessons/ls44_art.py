import turtle as t
from random import random

LEFT = 1.0
RIGHT = -1.0
TRUNK = 100.0
UP = 90.0

random_float: float = random()

def tree(x: float, y: float) -> None:
    t.penup()
    t.goto(x, y)
    t.pendown()
    branch(TRUNK, 90.0)
    t.update()


def branch(length: float, angle: float) -> None:
    t.setheading(angle)
    t.forward(length)
    if length < 3:
        ...
    else:
        branch(length * 0.7, angle + 25)
        branch(length * 0.6, angle - 25)
    t.setheading(angle + 180)
    t.forward(length)

if __name__ == "__main__":
    t.speed(0)
    t.tracer(0, 0)
    t.getscreen().onclick(tree)
    t.done()