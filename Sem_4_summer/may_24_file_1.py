from tkinter import *
from PIL import Image, ImageTk

# widgets - GUI elements: buttons, text boxes, labels, images
# windows - serves as a container to hold or contain these widgets
# label - an area widget that holds text and/or an image within a window

window = Tk()  # instantiate an instance of a Window

img_path = "C:\\Users\\HP\\Desktop\\wallpapers\\13.png"
img = Image.open(img_path)
img_resize = img.resize((355, 200))
photo = ImageTk.PhotoImage(img_resize)


label = Label(window,
              text="I am Vadisetti Pranay Satvik Reddy.\n I am on 9 tails form right now!!",
              font=('Arial', 20, 'underline'),
              foreground='Orange',
              background='Black',
              relief=RAISED,
              borderwidth=10,
              padx=20,
              pady=20,
              image=photo,
              compound='left')

label.photo = photo
label.pack()
# label.place(x=100, y=200)

window.title("My first Python GUI program")
icon_image = Image.open('indra.jpg')
icon = ImageTk.PhotoImage(icon_image)
window.iconphoto(True, icon)
window.config(background="#3cfcff")
# window.geometry("200x200")

window.mainloop()  # place window on computer screen, listen for events

