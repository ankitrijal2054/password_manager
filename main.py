from tkinter import*
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    with open("data_file.txt", mode='a') as data:
        data.write(f"Website: {website}  |  Email/Username: {email}  |  Password: {password}\n")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#creating all label
web_label = Label(text="Website:", font=("Arial", 12, "bold"))
web_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", font=("Arial", 12, "bold"))
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=("Arial", 12, "bold"))
password_label.grid(column=0, row=3)

##creating all entry
website_entry = Entry(width=51)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=51)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "ankitrijal88@gmail.com")

password_entry = Entry(width=33,)
password_entry.grid(column=1, row=3)

#creating all button
generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()