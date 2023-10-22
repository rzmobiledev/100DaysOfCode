from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.get_score(mode="r")
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def get_score(self, mode: str):
        with open("data.txt", mode=mode) as f:
            if mode == "w":
                f.write(f"{self.high_score}")
            else:
                self.high_score = int(f.read())

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score {self.score} High Score: {self.high_score}", align="center", font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.get_score(mode="w")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()