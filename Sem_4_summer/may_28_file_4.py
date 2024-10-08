import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *


def change_colour():
    colour = colorchooser.askcolor(title="choose colour")
    text_area.config(fg=colour[1])


def change_font(*args):
    text_area.config(font=(font_name.get(), font_size.get()))


def open_file():
    file = askopenfilename(defaultextension=".txt",
                       filetypes=[("Text Docs", ".txt"),
                                  ("All Files", "*.*")])

    try:
        window.title(os.path.basename(file))
        text_area.delete("1.0", END)
        file = open(file, 'r')
        text_area.insert("1.0", file.read())

    except Exception:
        print("Something Went Wrong in Opening a File")

    finally:
        file.close()


def save_file():
    file = filedialog.asksaveasfilename(initialfile="untitled.txt",
                                        defaultextension=".txt",
                                        filetypes=[("Text Docs", "*.txt"),
                                                   ("All Files", "*.*")])

    if file is None:
        return

    else:
        try:
            window.title(os.path.basename(file))
            file = open(file, "w")
            file.write(text_area.get("1.0", END))

        except Exception:
            print("An Error Occured While Saving")

        finally:
            file.close()


def new_file():
    window.title("Untitled")
    text_area.delete("1.0", END)


def cut():
    text_area.event_generate("<<Cut>>")


def copy():
    text_area.event_generate("<<Copy>>")


def paste():
    text_area.event_generate("<<Paste>>")


def about():
    showinfo("About this Text Editor", "This text editor is still"
                                       "under developement.\nFor any queries and "
                                       "business deals,\ncontact: 9059050444\n"
                                       "email: satvikvadisetti@gmail.com")


def quit_program():
    window.destroy()


window = Tk()
window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width - window_width) / 2)
y = int((screen_height - window_height) / 2)
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))
window.title("Text Editor Program")

font_name = StringVar(window)
font_name.set("Consolas")

font_size = StringVar(window)
font_size.set("25")

text_area = Text(window, font=(font_name.get(), font_size.get()))
scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky="nesw")
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

frame = Frame(window)
frame.grid()

colour_button = Button(frame, text="Colour", command=change_colour)
colour_button.grid(row=0, column=0)

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

size_box = Spinbox(frame, from_=1, to=200, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit_program)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

window.mainloop()
