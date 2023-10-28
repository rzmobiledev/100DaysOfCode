import tkinter

window = tkinter.Tk()
window.title("My First Gui Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am label", font=("Arial", 24, "bold"))
my_label.grid(column=1, row=0)
my_label.config(padx=20, pady=20)

def change_label():
    new_text = input.get()
    my_label["text"] = new_text


# Button
button = tkinter.Button(text="Click me", command=change_label)
button.grid(column=1, row=1)

new_btn = tkinter.Button(text="New Button")
new_btn.grid(column=3, row=0)

# Entry
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)



window.mainloop()