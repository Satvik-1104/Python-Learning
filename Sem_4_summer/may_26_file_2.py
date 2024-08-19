from tkinter import *
from tkinter import filedialog


def savefile():
    file = filedialog.asksaveasfile(defaultextension=".txt",
                                    filetypes=[
                                        ("text file", ".txt"),
                                        ("C", ".c"),
                                        ("HTML", ".html")
                                    ])

    if file is None:
        return

    filetext = input("Enter some text, okay?: ")
    file.write(filetext)
    file.close()


def readfile():
    filepath = filedialog.askopenfilename(filetypes=[
        ("text file", "*.txt"),
        ("C", "*.c"),
        ("HTML", "*.html")
    ])

    if filepath is None:
        return

    with open(filepath) as file:
        print(file.read())


def cut():
    print("You cut the file")


def copy():
    print("You copied the file")


def paste():
    print("You pasted the file")


window = Tk()

menubar = Menu(window)
window.config(menu=menubar)

file_menu = Menu(menubar,
                 font=("MV Boli", 15),
                 tearoff=0)

menubar.add_cascade(label= "File", menu=file_menu)
file_menu.add_command(label="Save", command=savefile)
file_menu.add_command(label="Read", command=readfile)
file_menu.add_separator()
file_menu.add_command(label="Quit", command=quit)

edit_menu = Menu(menubar,
                 font=("MV Boli", 15),
                 tearoff=0)

menubar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

window.mainloop()
