from tkinter import *
from PIL import Image, ImageTk

chocolates = 0


def count():
    global chocolates
    chocolates += 1
    print("You want " + str(chocolates) + " chocolates.")


window = Tk()

button = Button(window,
                text="How many chocolates do you want?",
                command=count,
                foreground='Green',
                background='Black',
                padx=20,
                pady=20,
                activeforeground='Black',
                activebackground='Green')

button.pack()

window.title("Button GUI")
window.config(background='Cyan')
img = Image.open('indra.jpg')
icon = ImageTk.PhotoImage(img)
window.iconphoto(True, icon)

window.mainloop()
