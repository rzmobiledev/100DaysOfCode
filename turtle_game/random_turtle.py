import turtle as t
from random import random, choice

colours = ("CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen")
direction = (0, 90, 180, 270)

for i in range(200):
    t.color(choice(colours))
    t.pensize(10)
    t.forward(30)
    t.setheading(choice(direction))

t.Screen().mainloop()
t.exitonclick()