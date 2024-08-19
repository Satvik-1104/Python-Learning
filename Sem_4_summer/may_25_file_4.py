# text widget - functions like a text area, you can enter multiple lines
#               of text

from tkinter import *


def submit():
    data = text.get("1.0", END)
    print(data)


window = Tk()

text = Text(
    window,
    background='light yellow',
    foreground='red',
    font=('ink free', 25),
    padx=10,
    pady=15,
    width=30,
    height=15
)

text.pack()

button = Button(
    window,
    text="submit",
    font=('Consolas', 10),
    command=submit
)

button.pack()

window.mainloop()
