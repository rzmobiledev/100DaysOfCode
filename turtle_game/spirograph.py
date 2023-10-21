import random
import turtle
import turtle as t

tim = t.Turtle()
t.colormode(255)

def random_color() -> tuple:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


tim.pensize(1)
tim.speed("fastest")


def draw_spirograph(size_of_gap: int):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(2)
t.Screen().exitonclick()