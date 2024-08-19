from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window)

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text="TAB1")
notebook.add(tab2, text="TAB2")
notebook.pack(expand=True, fill="both")

Label(tab1,
      text="HELLLO, I am TAB1 and I am representing HELLO",
      font=("Ink Free", 25),
      background="black",
      foreground="whitesmoke").pack(anchor=CENTER)

Label(tab2,
      text="BYEEEE, I am TAB2 and I am representing BYE",
      font=("Ink Free", 25),
      background="black",
      foreground="whitesmoke").pack(anchor=CENTER)

window.mainloop()
