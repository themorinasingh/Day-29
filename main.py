from tkinter import *
from tkinter import messagebox
from passGen import password_generator
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    password = password_generator()
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_name.get()
    username = email_input.get()
    password = password_input.get()

    if len(website) < 1 or len(password) < 1 or len(email) <1:
        messagebox.showinfo(title="OOPS!" ,message="Please don't leave any fields Empty!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Do you want to save these details?"
                                                           f"\nEmail/Username: {username}"
                                                           f"\nPassword: {password}")

        if is_ok:
            with open("data.txt", "a") as data:

                data.write(f"{website} | {username} | {password}\n")

            website_name.delete(0, END)
            password_input.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#creating the canvas and importing image
canvas = Canvas(width=200, height=200)
image = PhotoImage(file="./logo.png")
logo = canvas.create_image(100,90, image=image)
canvas.grid(column=1, row=0)

#creating Labels and entry
#todo website label
website_label = Label(text="Website: ")
website_label.grid(column= 0, row= 1)

website_name = Entry()
website_name.config(width=35)
website_name.grid(column=1,row=1, columnspan=2 )
website_name.focus()

#todo email/username label and entry
email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

email_input = Entry()
email_input.config(width=35)
email_input.insert(END,"theogmoe@thecyberdude.com" )
email_input.grid(column=1,row=2, columnspan=2)

#todo creating the password label and entry
password_label = Label()
password_label.config(text="Password: ")
password_label.grid(column= 0,row=3 )

password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky=E)

#todo create buttons

# Generate Password Button
generate_password_button = Button(text="Generate Password", width=10, command=password_gen )
generate_password_button.grid(column=2, row=3, sticky=W)

# Add Button


add_button = Button()
add_button.config(text="Add", width=34, borderwidth=0, command=save_data)
add_button.grid(column=1, row=4 , columnspan=2)
















window.mainloop()