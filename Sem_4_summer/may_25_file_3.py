from tkinter import *
from tkinter import colorchooser


def click():
    colour = colorchooser.askcolor()
    colour_hex = colour[1]
    print(colour_hex)
    window.config(background=colour_hex)


window = Tk()

window.geometry("420x420")
button = Button(text="click me",
                font=("Consolas", 10),
                command=click)

button.pack()

window.mainloop()
