from tkinter import*
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list += (choice(letters) for _ in range(randint(8, 10)))
    password_list += (choice(symbols) for _ in range(randint(2, 4)))
    password_list += (choice(numbers) for _ in range(randint(2, 4)))

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password_entry.get())

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fiels empty!")
    else:
        is_ok = messagebox.askyesno(title=website, message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\n"
                                               f"Do you want to save it?")
        if is_ok:
            with open("data_file.txt", mode='a') as data:
                data.write(f"Website: {website}  |  Email/Username: {email}  |  Password: {password}\n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)


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
generate_button = Button(text="Generate Password", command=password_gen)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()