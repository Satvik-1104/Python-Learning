from tkinter import *
from PIL import Image, ImageTk


def check_box():
    if x.get() == 1:
        print("Thanks for coming to my Birthday Party")
    else:
        print("Fuck OFF!")


window = Tk()

img = Image.open("indra.jpg")
resized_img = img.resize((36, 20))
icon = ImageTk.PhotoImage(resized_img)

x = IntVar()

check_button = Checkbutton(window,
                           text="Check if ""YES""",
                           font=('Arial', 20, 'bold'),
                           variable=x,
                           command=check_box,
                           onvalue=1,
                           offvalue=0,
                           background="#7E909A",
                           foreground="#23282D",
                           activebackground="#23282D",
                           activeforeground="#7E909A",
                           pady=10,
                           padx=25,
                           image=icon,
                           compound="left")

check_button.pack()

window.mainloop()
