import turtle as t

tim = t.Turtle()

looping = [
    {
        "range": 3,
        "color": "blue",
        "turn_right": 120,
        "forward": 100
    },

    {
        "range": 4,
        "color": "red",
        "turn_right": 90,
        "forward": 100
    },
    {
        "range": 5,
        "color": "green",
        "turn_right": 72,
        "forward": 100
    },

    {
        "range": 6,
        "color": "orange",
        "turn_right": 60,
        "forward": 100
    },
    {
        "range": 7,
        "color": "purple",
        "turn_right": 51,
        "forward": 100
    },
    {
        "range": 8,
        "color": "magenta",
        "turn_right": 45,
        "forward": 100
    }
]

for i in looping:
    for _ in range(i['range']):
        t.color(i['color'])
        t.right(i['turn_right'])
        t.forward(i['forward'])

t.Screen()
t.exitonclick()
