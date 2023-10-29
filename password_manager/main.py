import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- SEARCH RESULT ------------------------------------ #

def search():
    try:
        with open("data.json", "r") as file_data:
            data = json.load(file_data)
            website = website_entry.get()
            email = data[website].get('email')
            password = data[website].get('password')
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="File not found!\nTry to create a new one.")
    except KeyError:
        messagebox.showerror(title="Not Found", message="Data not found")
    else:
        messagebox.showinfo(title="Data found", message=f"Here is data you are looking for\n"
                            f"Website: {website}\nEmail: {email}\nPassword: {password}")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
        'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'o', 'p',
        'q', 'r', 's', 't', 'u'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_numbers + password_letters + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")

    else:
        try:
            with open("data.json", "r") as data_file:

                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

                website_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)
        else:
            with open("data.json", "w") as data_file:
                # updating old data with new data
                data.update(new_data)
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(height=200, width=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = tk.Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = tk.Label(text="Password")
password_label.grid(row=3, column=0)

# Entries
website_entry = tk.Entry(width=26)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = tk.Entry(width=36)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "rzmobiledev@gmail.com")
password_entry = tk.Entry(width=26)
password_entry.grid(row=3, column=1)

# Button
generate_password_button = tk.Button(text="Generate", font=("Courier", 8, "bold"), command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = tk.Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)

# Search
search_btn = tk.Button(text="Search", font=("Courier", 8, "bold"), command=search)
search_btn.grid(row=1, column=2)

window.mainloop()
