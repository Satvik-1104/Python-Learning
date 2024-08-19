from tkinter import *
from tkinter import messagebox


def click():
    # messagebox.showerror(title="Error message", message="Your coding SUCKS!")
    # messagebox.showinfo(title="Info message", message="The phone you bought is a GOOD one")
    # messagebox.showwarning(title="Warning message", message="Don't play FF for too long")

    # print(messagebox.askokcancel(title="ok cancel", message="Is it okay to play FF now?"))
    # print(messagebox.askyesno(title="yes no", message="Is it okay to play FF now?"))
    # print(messagebox.askquestion(title="ask question", message="Is it okay to play FF now?"))
    # print(messagebox.askretrycancel(title="retry cancel", message="Is it okay to play FF now?"))
    print(messagebox.askyesnocancel(title="yes no cancel", message="Is it okay to play FF now?"))


window = Tk()

button = Button(window,
                text="click me",
                font=('Consolas', 15),
                command=click)

button.pack()

window.mainloop()