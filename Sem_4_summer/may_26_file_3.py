# frame - a rectangular container to group and hold widgets

# Creating new Windows -
#                       Toplevel() - new old_window 'on top' of other windows,
#                                    linked to the bottom old_window
#                                    top level old_window will be closed if
#                                    bottom old_window is closed
#                       Tk() - create a new independent old_window

from tkinter import *
from tkinter import ttk


def create_window():
    new_window = Tk()
    # new_window = Toplevel()
    old_window.destroy()  # to close the old window


old_window = Tk()

frame = Frame(old_window,
              background="white",
              relief=RAISED,
              borderwidth=5)
frame.pack()

w = Button(frame,
           text="W",
           font=("Consolas", 25),
           width=3, relief=RAISED,
           borderwidth=10,
           background="black",
           foreground="whitesmoke")
w.pack(side=TOP)

a = Button(frame,
           text="A",
           font=("Consolas", 25),
           width=3, relief=RAISED,
           borderwidth=10,
           background="black",
           foreground="whitesmoke")
a.pack(side=LEFT)

s = Button(frame,
           text="S",
           font=("Consolas", 25),
           width=3, relief=RAISED,
           borderwidth=10,
           background="black",
           foreground="whitesmoke")
s.pack(side=LEFT)

d = Button(frame,
           text="D",
           font=("Consolas", 25),
           width=3, relief=RAISED,
           borderwidth=10,
           background="black",
           foreground="whitesmoke")
d.pack(side=LEFT)

new = Button(old_window,
             text="create new empty window",
             font=("Consolas", 13),
             padx=7.4,
             relief=RAISED,
             borderwidth=10,
             background="black",
             foreground="whitesmoke",
             command=create_window)
new.pack()

old_window.mainloop()
