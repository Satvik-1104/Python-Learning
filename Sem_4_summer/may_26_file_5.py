import time
from tkinter import *
from tkinter.ttk import *

# grid() - geometry manager that organizes widgets in a table-like
#          structure


def submit():
    print("First name: " + firstname_entry.get())
    print("Last name: " + lastname_entry.get())
    print("Full name: " + firstname_entry.get() + " " + lastname_entry.get())
    print("Email: " + email_entry.get())


def start():
    submit_button.config(state=DISABLED)
    tasks = 1250
    done = 0
    while done < tasks:
        time.sleep(0.01)
        bar['value'] += (5/1250) * 100
        done += 5
        percent.set(str(int((done/tasks) * 100)) + "% of submission done")
        window.update_idletasks()
    submit()


window = Tk()

percent = StringVar()

headlabel = Label(window,
                  text="ENTER YOUR INFO",
                  foreground="Violet",
                  background="Cyan",
                  font=("Consolas", 25, "bold"))

firstname_label = Label(window,
                        text="First name: ",
                        foreground="Whitesmoke",
                        background="Black",
                        font=("Ink Free", 15))

firstname_entry = Entry(window,
                        foreground="Black",
                        background="Whitesmoke",
                        font=("Ink Free", 15, "bold"),
                        width=50)

lastname_label = Label(window,
                       text="Last name: ",
                       foreground="Whitesmoke",
                       background="Black",
                       font=("Ink Free", 15))

lastname_entry = Entry(window,
                       foreground="Black",
                       background="Whitesmoke",
                       font=("Ink Free", 15, "bold"),
                       width=50)

email_label = Label(window,
                    text="Email: ",
                    foreground="Whitesmoke",
                    background="Black",
                    font=("Ink Free", 15))

email_entry = Entry(window,
                    foreground="Black",
                    background="Whitesmoke",
                    font=("Ink Free", 15, "bold"),
                    width=50)

submit_button = Button(window,
                       text="Submit",
                       command=start)

bar = Progressbar(window,
                  orient=HORIZONTAL,
                  length=400)

percent_label = Label(window,
                      textvariable=percent)

headlabel.grid(row=0, column=0, columnspan=2)
firstname_label.grid(row=1, column=0)
firstname_entry.grid(row=1, column=1)
lastname_label.grid(row=2, column=0)
lastname_entry.grid(row=2, column=1)
email_label.grid(row=3, column=0)
email_entry.grid(row=3, column=1)
submit_button.grid(row=4, column=0, columnspan=2)
bar.grid(row=5, column=0, columnspan=2)
percent_label.grid(row=6, column=0, columnspan=2)

window.mainloop()
