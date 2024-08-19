from tkinter import *
from may_27_file_6 import *
import time

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volleyBall = Ball(canvas, 0, 0,
                  100, 2, 3, "Yellow")
tennisBall = Ball(canvas, 0, 0,
                  50, 5, 6, "Lime")
cricketBall = Ball(canvas, 0, 0,
                  50, 8, 3, "Red")
pingpongBall = Ball(canvas, 0, 0,
                  20, 2, 9, "Cyan")
footBall = Ball(canvas, 0, 0,
                100, 4, 5, "black")

while True:
    volleyBall.move()
    tennisBall.move()
    cricketBall.move()
    pingpongBall.move()
    footBall.move()
    window.update()
    time.sleep(0.01)

window.mainloop()