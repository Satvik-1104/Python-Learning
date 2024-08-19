from tkinter import *
from PIL import Image, ImageTk

window = Tk()


def delete(entry):
    entry.delete(0, END)


def backspace(entry):
    entry.delete(len(entry.get()) - 1, END)


def user_name_submit(entry):
    print("username: " + entry.get())
    entry.config(state=DISABLED)


def password_submit(entry):
    print("password: " + entry.get())
    entry.config(state=DISABLED)


username = Entry(window,
              font=('Arial', 20),
              foreground='Red',
              background='Cyan',
              )

username.grid(row=0, column=0, padx=5, pady=5)

submit_button = Button(window,
                text="Submit",
                command=lambda: user_name_submit(username))

submit_button.grid(row=0, column=1, padx=5, pady=5)

backspace_button = Button(window,
                text="Backspace",
                command=lambda: backspace(username))

backspace_button.grid(row=0, column=2, padx=5, pady=5)

delete_button = Button(window,
                text="Delete",
                command=lambda: delete(username))

delete_button.grid(row=0, column=3, padx=5, pady=5)

password = Entry(window,
              font=('Arial', 20),
              foreground='Red',
              background='Cyan',
              show="*"
              )

password.grid(row=1, column=0, padx=5, pady=5)

submit_button = Button(window,
                text="Submit",
                command=lambda: password_submit(password))

submit_button.grid(row=1, column=1, padx=5, pady=5)

backspace_button = Button(window,
                text="Backspace",
                command=lambda: backspace(password))

backspace_button.grid(row=1, column=2, padx=5, pady=5)

delete_button = Button(window,
                text="Delete",
                command=lambda: delete(password))

delete_button.grid(row=1, column=3, padx=5, pady=5)

window.mainloop()
