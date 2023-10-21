from turtle import Turtle, Screen


timmy = Turtle()
timmy.shape("turtle")
timmy.color("red", "green")

for _ in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
timmy.left(90)

screen = Screen()
screen.exitonclick()