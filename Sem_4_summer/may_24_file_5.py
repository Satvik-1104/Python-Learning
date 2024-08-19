from tkinter import *
from PIL import Image, ImageTk


def order():
    for i in range(len(radiobuttons)):
        radiobuttons[i].config(state=DISABLED)
    if x.get() == 0:
        print("You have ordered a Ducati Diavel V4")
    elif x.get() == 1:
        print("You have ordered a Harley Davidson Fatbob")
    elif x.get() == 2:
        print("You have ordered a Triumph Rocket III")


def budget():
    print("The budget for the bike is " + str(y.get()) + "000$")
    scale.config(state=DISABLED)


window = Tk()

bikes = ["Ducati Diavel V4", "Harley Davidson Fatbob", "Triumph Rocket III"]
x = IntVar()
y = IntVar()

ducati_img = Image.open('ducati diavel v4.jpg')
resized_ducati_img = ducati_img.resize((53, 30))
ducati_image = ImageTk.PhotoImage(resized_ducati_img)

harley_img = Image.open('harley davidson fatbob.jpg')
resized_harley_img = harley_img.resize((48, 30))
harley_image = ImageTk.PhotoImage(resized_harley_img)

triumph_img = Image.open('triumph rocket III.jpg')
resized_triumph_img = triumph_img.resize((44, 30))
triumph_image = ImageTk.PhotoImage(resized_triumph_img)

images = [ducati_image, harley_image, triumph_image]
radiobuttons = []

for index in range(len(bikes)):
    radiobutton = Radiobutton(window,
                              text=bikes[index],
                              font=("Impact", 30),
                              padx=10,
                              pady=30,
                              variable=x,
                              value=index,
                              image=images[index],
                              command=order,
                              compound='left',
                              background='lime',
                              foreground='black',
                              activeforeground='black',
                              activebackground='lime',
                              width = 450
                              )
    radiobutton.pack(anchor=W)
    radiobuttons.append(radiobutton)

scale = Scale(window,
              from_=17,
              to=36,
              length=375,
              orient=HORIZONTAL,
              font=('Consolas', 12),
              tickinterval=2,
              resolution=1,
              background='black',
              foreground='orange',
              troughcolor='cyan',
              variable=y
              )

scale.pack()

submit = Button(window,
                text='Submit',
                font=('Consolas', 15),
                command=budget)

submit.pack()

window.title("BIKE SELECTION")
window.config(background='lime')

window.mainloop()
