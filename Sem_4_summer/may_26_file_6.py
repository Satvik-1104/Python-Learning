# canvas - widget that is used ro draw graphs, plots or images in a window

from tkinter import *


def do_something(event):
    print("Mouse Coordinates: " + str(event.x) + ", " + str(event.y))


window = Tk()

window.bind("<Button-1>", do_something)  # left click
# window.bind("<Button-2>", do_something)  # scroll click
# window.bind("<Button-3>", do_something)  # right click
# window.bind("<ButtonRelease>", do_something)  # any mouse button release
# window.bind("<Enter>", do_something)  # window enter point
# window.bind("<Leave>", do_something)  # window leave point
# window.bind("<Motion>", do_something)  # where the mouse moves

canvas = Canvas(window,
                height=500,
                width=500)

canvas.create_rectangle(125, 200, 375, 450, fill="Light yellow")
canvas.create_polygon(250, 65, 80, 200, 420, 200, fill="Brown")
canvas.create_rectangle(200, 300, 300, 450, fill="Green")
canvas.create_oval(283, 370, 293, 380, fill="Goldenrod")
canvas.create_arc(200, 225, 300, 325, extent=180, fill="Cyan")

canvas.pack()

window.mainloop()
