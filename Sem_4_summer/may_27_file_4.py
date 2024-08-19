from tkinter import *
from PIL import Image, ImageTk
import time

velocityX = 0.1
velocityY = 2

window = Tk()

canvas = Canvas(window, width=800, height=450)
canvas.pack()

bg_image = Image.open('ducati diavel v4.jpg')
background_image = ImageTk.PhotoImage(bg_image)
background = canvas.create_image(0, 0, image=background_image, anchor=NW)

move_image = PhotoImage(file='racecar.png')
race_car = canvas.create_image(0, 0, image=move_image, anchor=NW)

race_car_width = move_image.width()
race_car_height = move_image.height()

while True:
    coordinates = canvas.coords(race_car)
    print(coordinates)
    if coordinates[0] < 0 or coordinates[0] >= 800 - race_car_width:
        velocityX = -velocityX
    if coordinates[1] < 0 or coordinates[1] >= 450 - race_car_height:
        velocityY = -velocityY
    canvas.move(race_car, velocityX, velocityY)
    window.update()
    time.sleep(0.01)

window.mainloop()
