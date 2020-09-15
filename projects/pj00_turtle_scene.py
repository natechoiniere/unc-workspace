"""TODO: Describe your scene program."""

__author__ = "730443739"

from turtle import Turtle, bgcolor, done


def main() -> None:
    """The entrypoint of my scene."""
    # TODO: Declare your turtle variable(s) here.
    urkel: Turtle = Turtle()
    urkel.speed(50)
    border: Turtle = Turtle()
    i: int = 0
    
    # Drawing the border
    bgcolor("lightblue")
    border.hideturtle()
    border.speed(50)
    border.penup()
    border.setposition(-300, -300)
    border.pendown()
    border.fillcolor("black")
    border.pencolor("black")
    border.pensize(3)
    while i < 4:
        border.forward(600)
        border.left(90)
        i += 1


# TODO: Call the procedures you define and pass your Turtle(S) as an argument
    draw_rect(urkel, "green", True, -300, -300, 600, 200)
    draw_rect(urkel, "brown", True, -200, -100, 180, 180)
    draw_rect(urkel, "black", True, -130, -100, 40, 60)
    draw_rect(urkel, "white", True, -160, 30, 20, 30)
    draw_rect(urkel, "white", True, -80, 30, 20, 30)
    draw_rect(urkel, "white", True, -80, -30, 20, 30)
    draw_rect(urkel, "white", True, -160, -30, 20, 30)
    draw_rect(urkel, "red4", True, 100, -100, 30, 200,)
    draw_circle(urkel, "yellow", True, 50, -220, 150)
    draw_circle(urkel, "DarkGreen", True, 50, 50, 50)
    draw_circle(urkel, "DarkGreen", True, 50, 100, 100)
    draw_circle(urkel, "DarkGreen", True, 50, 150, 100)
    draw_circle(urkel, "DarkGreen", True, 50, 100, 50)
    draw_circle(urkel, "DarkGreen", True, 50, 120, 30)
    draw_circle(urkel, "DarkGreen", True, 80, 120, 30)


# TODO: Define the procedures for other components in your scene here.
def draw_circle(turtle: Turtle, color: str, fill: bool, radius: float, posx: float, posy: float) -> None:
    """This function draws a circle with the given turtle, color, radius, and position."""
    turtle.penup()
    turtle.hideturtle()
    turtle.setpos(posx, posy)
    if fill == True:
        turtle.setheading(0)
        turtle.pencolor(color)
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.circle(radius)  # Using the Turtle documenation to do this, with the circle() function.
        turtle.end_fill()
    else:
        turtle.pencolor(color)
        turtle.circle(radius) 


def draw_rect(turtle: Turtle, color: str, fill: bool, posx: float, posy: float, length: float, height: float) -> None:
    """This function draws a rectangle with the given turtle, color, length, height, and position."""
    turtle.penup()
    turtle.hideturtle()
    turtle.setpos(posx, posy)
    if fill == True:
        k: int = 0
        turtle.setheading(0)
        turtle.pencolor(color)
        turtle.fillcolor(color)
        turtle.begin_fill()
        while k < 2:
            turtle.forward(length)
            turtle.left(90)
            turtle.forward(height)
            turtle.left(90)
            k += 1
        turtle.end_fill()
    else:
        k = 0
        turtle.setheading(0)
        turtle.pencolor(color)
        while k < 2:
            turtle.forward(length)
            turtle.left(90)
            turtle.forward(height)
            turtle.left(90)
            k += 1


# Python idiom (convention) for a runnable Python module.
if __name__ == "__main__":
    main()
done()