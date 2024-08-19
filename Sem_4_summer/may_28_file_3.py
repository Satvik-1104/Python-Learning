from tkinter import *


def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total

    except ZeroDivisionError:
        equation_label.set("Infinity")
        equation_text = ""

    except SyntaxError:
        equation_label.set("Syntax Error")
        equation_text = ""


def clear():
    global equation_text
    equation_text = ""
    equation_label.set("")


window = Tk()
window.title("Calculator")
window.geometry("445x455")
window.config(background="black")
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_columnconfigure(3, weight=1)
window.grid_rowconfigure(4, weight=1)
window.grid_rowconfigure(5, weight=1)
window.grid_rowconfigure(6, weight=1)

equation_text = ""

equation_label = StringVar()

entry = Entry(window, textvariable=equation_label, font =("Consolas", 30),
              background="black", foreground="whitesmoke", borderwidth=0)

entry.grid(row=0, columnspan=4, pady=30)

button_pl = Button(window, text="(", font=("Consolas", 15), relief=RAISED,
                   borderwidth=5, command=lambda: button_press("("),
                   background="Whitesmoke", foreground="Black",
                   height=2, width=6, activebackground="#007EA7",
                   activeforeground="#E5F3FD")
button_pl.grid(row=2, column=0, sticky="nsew")

button_pr = Button(window, text=")", font=("Consolas", 15), relief=RAISED,
                   borderwidth=5, command=lambda: button_press(")"),
                   background="Whitesmoke", foreground="Black",
                   height=2, width=6, activebackground="#007EA7",
                   activeforeground="#E5F3FD")
button_pr.grid(row=2, column=1, sticky="nsew")

button_perc = Button(window, text="%", font=("Consolas", 15), relief=RAISED,
                     borderwidth=5, command=lambda: button_press("%"),
                     background="Whitesmoke", foreground="Black",
                     height=2, width=6, activebackground="#007EA7",
                     activeforeground="#E5F3FD")
button_perc.grid(row=2, column=2, sticky="nsew")

button_AC = Button(window, text="AC", font=("Consolas", 15), relief=RAISED,
                   borderwidth=5, command=clear,
                   background="Whitesmoke", foreground="Black",
                   height=2, width=6)
button_AC.grid(row=2, column=3, sticky="nsew")

button_1 = Button(window, text=1, font=("Consolas", 15), relief=RAISED,
                  borderwidth=5, command=lambda: button_press(1),
                  background="Whitesmoke", foreground="Black",
                  height=2, width=6, activebackground="#007EA7",
                  activeforeground="#E5F3FD")
button_1.grid(row=3, column=0, sticky="nsew")

button_2 = Button(window, text=2, font=("Consolas", 15), relief=RAISED,
                  borderwidth=5, command=lambda: button_press(2),
                  background="Whitesmoke", foreground="Black",
                  height=2, width=6, activebackground="#007EA7",
                  activeforeground="#E5F3FD")
button_2.grid(row=3, column=1, sticky="nsew")

button_3 = Button(window, text=3, font=("Consolas", 15), relief=RAISED,
                  borderwidth=5, command=lambda: button_press(3),
                  background="Whitesmoke", foreground="Black",
                  height=2, width=6, activebackground="#007EA7",
                  activeforeground="#E5F3FD")
button_3.grid(row=3, column=2, sticky="nsew")

button_div = Button(window, text="/", font=("Consolas", 15), relief=RAISED,
                    borderwidth=5, command=lambda: button_press("/"),
                    background="#FC7126", foreground="Whitesmoke",
                    height=2, width=6, activebackground="#007EA7",
                    activeforeground="#E5F3FD")
button_div.grid(row=3, column=3, sticky="nsew")

button_4 = Button(window, text=4, font=("Consolas", 15), relief=RAISED,
                  borderwidth=5, command=lambda: button_press(4),
                  background="Whitesmoke", foreground="Black",
                  height=2, width=6, activebackground="#007EA7",
                   activeforeground="#E5F3FD")
button_4.grid(row=4, column=0, sticky="nsew")

button_5 = Button(window, text=5, font=("Consolas", 15), relief=RAISED,
                  borderwidth=5, command=lambda: button_press(5),
                  background="Whitesmoke", foreground="Black",
                  height=2, width=6, activebackground="#007EA7",
                  activeforeground="#E5F3FD")
button_5.grid(row=4, column=1, sticky="nsew")

button_6 = Button(window, text=6, font=("Consolas", 15), relief=RAISED,
                  borderwidth=5, command=lambda: button_press(6),
                  background="Whitesmoke", foreground="Black",
                  height=2, width=6, activebackground="#007EA7",
                  activeforeground="#E5F3FD")
button_6.grid(row=4, column=2, sticky="nsew")

button_mul = Button(window, text="*", font=("Consolas", 15), relief=RAISED,
                    borderwidth=5, command=lambda: button_press("*"),
                    background="#FC7126", foreground="Whitesmoke",
                    height=2, width=6, activebackground="#007EA7",
                    activeforeground="#E5F3FD")
button_mul.grid(row=4, column=3, sticky="nsew")

button_7 = Button(window, text=7, font=("Consolas", 15), relief=RAISED,
                  borderwidth=5, command=lambda: button_press(7),
                  background="Whitesmoke", foreground="Black",
                  height=2, width=6, activebackground="#007EA7",
                  activeforeground="#E5F3FD")
button_7.grid(row=5, column=0, sticky="nsew")

button_8 = Button(window, text=8, font=("Consolas", 15), relief=RAISED,
                  borderwidth=5, command=lambda: button_press(8),
                  background="Whitesmoke", foreground="Black",
                  height=2, width=6, activebackground="#007EA7",
                  activeforeground="#E5F3FD")
button_8.grid(row=5, column=1, sticky="nsew")

button_9 = Button(window, text=9, font=("Consolas", 15), relief=RAISED,
                  borderwidth=5, command=lambda: button_press(9),
                  background="Whitesmoke", foreground="Black",
                  height=2, width=6, activebackground="#007EA7",
                  activeforeground="#E5F3FD")
button_9.grid(row=5, column=2, sticky="nsew")

button_min = Button(window, text="-", font=("Consolas", 15), relief=RAISED,
                    borderwidth=5, command=lambda: button_press("-"),
                    background="#FC7126", foreground="Whitesmoke",
                    height=2, width=6, activebackground="#007EA7",
                    activeforeground="#E5F3FD")
button_min.grid(row=5, column=3, sticky="nsew")

button_0 = Button(window, text=0, font=("Consolas", 15), relief=RAISED,
                  borderwidth=5, command=lambda: button_press(0),
                  background="Whitesmoke", foreground="Black",
                  height=2, width=6, activebackground="#007EA7",
                  activeforeground="#E5F3FD")
button_0.grid(row=6, column=0, sticky="nsew")

button_dec = Button(window, text=".", font=("Consolas", 15), relief=RAISED,
                    borderwidth=5, command=lambda: button_press("."),
                    background="Whitesmoke", foreground="Black",
                    height=2, width=6, activebackground="#007EA7",
                    activeforeground="#E5F3FD")
button_dec.grid(row=6, column=1, sticky="nsew")

button_eq = Button(window, text="=", font=("Consolas", 15), relief=RAISED,
                   borderwidth=5, command=equals,
                   background="#C94802", foreground="Whitesmoke",
                   height=2, width=6, activebackground="#007EA7",
                   activeforeground="#E5F3FD")
button_eq.grid(row=6, column=2, sticky="nsew")

button_plus = Button(window, text="+", font=("Consolas", 15), relief=RAISED,
                     borderwidth=5, command=lambda: button_press("+"),
                     background="#FC7126", foreground="Whitesmoke",
                     height=2, width=6, activebackground="#007EA7",
                     activeforeground="#E5F3FD")
button_plus.grid(row=6, column=3, sticky="nsew")


window.mainloop()