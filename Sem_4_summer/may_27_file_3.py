from tkinter import *


def up(event):
    canvas.move(racecar, 0, -10)


def down(event):
    canvas.move(racecar, 0, 10)


def left(event):
    canvas.move(racecar, -10, 0)


def right(event):
    canvas.move(racecar, 10, 0)


window = Tk()

window.bind("<w>", up)
window.bind("<s>", down)
window.bind("<a>", left)
window.bind("<d>", right)
window.bind("<Up>", up)
window.bind("<Down>", down)
window.bind("<Left>", left)
window.bind("<Right>", right)

canvas = Canvas(window, width=500, height=500)
canvas.pack()

myImage = PhotoImage(file='racecar.png')
racecar = canvas.create_image(0, 0, image=myImage, anchor=NW)

window.mainloop()
