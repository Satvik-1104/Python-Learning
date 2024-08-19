from tkinter import *


def do_something(event):
    print("You pressed: " + event.keysym)
    label.config(text=event.keysym)


window = Tk()

window.bind("<Key>", do_something)

label = Label(window,
              font=("Helvetica", 100),
              background="black",
              foreground="Whitesmoke")
label.pack()

window.mainloop()
