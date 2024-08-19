from tkinter import *
from tkinter import filedialog
import os


def openfile():
    filepath = filedialog.askopenfilename(title="Open a file ok?",
                                          filetypes=(("text files", "*.txt"),
                                                     ("all files", "*.*")))

    if filepath is None:
        return

    with open(filepath) as file:
        print(file.read())


def savefile():
    file = filedialog.asksaveasfile(defaultextension=".txt",
                             filetypes=[
                                 ("Text file", ".txt"),
                                 ("C", ".c"),
                                 ("JAVA", ".java"),
                                 ("Python", ".py"),
                                 ("All files", ".*"),
                             ])

    if file is None:
        return

    file_text = str(text.get(1.0, END))
    file.write(file_text)


window = Tk()

open_button = Button(text="Read file", command=openfile)
open_button.pack()

save_button = Button(text="Save file", command=savefile)
save_button.pack()

text = Text(window)
text.pack()

window.mainloop()
