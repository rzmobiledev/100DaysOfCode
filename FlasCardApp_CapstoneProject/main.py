import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"


to_learn = {}
current_card = {}

try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def is_known():
    if not current_card:
        next_card()
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()

def flip_card():
    global current_card
    if not current_card:
        current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = tk.Canvas(width=800, height=526)
card_front_img = tk.PhotoImage(file="./images/card_front.png")
card_back_img = tk.PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# button
cross_image = tk.PhotoImage(file="./images/wrong.png")
unknown_button = tk.Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = tk.PhotoImage(file="./images/right.png")
known_button = tk.Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

window.mainloop()
