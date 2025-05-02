from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters = random.randint(5,10)
    nr_symbols = random.randint(5,10)
    nr_numbers = random.randint(5,10)
    password_list = []

    for char in range(1, nr_letters + 1):
        password_list.append(random.choice(letters))

    for char in range(1, nr_symbols + 1):
        password_list += random.choice(symbols)

    for char in range(1, nr_numbers + 1):
        password_list += random.choice(numbers)

    # print(password_list)
    random.shuffle(password_list)
    # print(password_list)

    password = ""
    for char in password_list:
        password += char

    # print(f"Your password is: {password}")
    password_entry.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if website=="" or password == "":
        messagebox.showerror(title="Error", message="Either email, or pass is empty.")
    else:
        # messagebox.showinfo(title="Title", message="This is a message.")
        is_ok = messagebox.askquestion(
            title=website,
            message=f"These are the details entered:\n Email: {email}\n Password: {password}\n"
            f"\n Is it Ok to save?",
        )
        if is_ok==True:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
            


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry()
website_entry.grid(row=1, column=1, ipadx=36)
website_entry.focus()
email_entry = Entry()
email_entry.grid(row=2, column=1, ipadx=36)
email_entry.insert(0, "email@domain.com")
password_entry = Entry()
password_entry.grid(row=3, column=1)

generate_pass_button = Button(text="Generate Password", command=password_generator)
generate_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", command=save)
add_button.grid(row=4, column=1)

window.mainloop()
