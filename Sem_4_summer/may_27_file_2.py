from tkinter import *


def up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() - 10)


def down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() + 10)


def left(event):
    label.place(x=label.winfo_x() - 10, y=label.winfo_y())


def right(event):
    label.place(x=label.winfo_x() + 10, y=label.winfo_y())


window = Tk()
window.geometry("500x500")

myImage = PhotoImage(file='racecar.png')
label = Label(window,
              image=myImage)

window.bind("<w>", up)
window.bind("<s>", down)
window.bind("<a>", left)
window.bind("<d>", right)
window.bind("<Up>", up)
window.bind("<Down>", down)
window.bind("<Left>", left)
window.bind("<Right>", right)

label.place(x=0, y=0)

window.mainloop()
