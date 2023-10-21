import random
import turtle
import turtle as t

tim = t.Turtle()

screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

game_is_on = False
colors = ("red", "orange", "yellow", "green", "blue", "purple")
y_position = (-70, -40, -10, 20, 50, 80)
all_turtles = []

def start_race():
    for index in range(6):
        turtles = t.Turtle(shape="turtle")
        turtles.color(colors[index])
        turtles.penup()
        turtles.goto(x=-230, y=y_position[index])
        all_turtles.append(turtles)


start_race()
if user_bet:
    game_is_on = True

while game_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            game_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()