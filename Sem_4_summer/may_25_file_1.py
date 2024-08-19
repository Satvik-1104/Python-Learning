# listbox - A listing of selectable text items within it's own container

from tkinter import *


def submit():
    bikes = []
    for index in list_box.curselection():
        bikes.insert(index, list_box.get(index))

    print("The bikes you have Wish-listed are: ")

    for index in bikes:
        print(index)


def delete():
    for index in reversed(list_box.curselection()):
        list_box.delete(index)
    list_box.config(height=list_box.size())


def add():
    list_box.insert(list_box.size(), entry_box.get())
    list_box.config(height=list_box.size())


window = Tk()

list_box = Listbox(window,
                   bg="#f7ffde",
                   font=('Constantia', 20),
                   width=30,
                   selectmode=MULTIPLE)

list_box.pack()

entry_box = Entry(window,
                  font=('Consolas', 10))

entry_box.pack()

add_button = Button(window,
                       text="Add",
                       font=('Consolas', 10),
                       command=add)

add_button.pack()

delete_button = Button(window,
                       text="Delete",
                       font=('Consolas', 10),
                       command=delete)

delete_button.pack()

submit_button = Button(window,
                       text="Submit",
                       font=('Consolas', 10),
                       command=submit)

submit_button.pack()

list_box.insert(1, "Triumph Bonneville Bobber")
list_box.insert(2, "Harley Davidson Hotrod")
list_box.insert(3, "Kawasaki Vulcan S")
list_box.insert(4, "Norton V4SE")
list_box.insert(5, "Jawa Perak")
list_box.insert(6, "Triumph Rocket III")

list_box.config(height=list_box.size())

window.mainloop()
