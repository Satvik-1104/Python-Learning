from tkinter import *
import random


def new_game():
    global player
    player = random.choice(players)
    label.config(text=player+"'s turn")
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", bg="#f8ccf9", fg="#7e4b8b",)


def check_winner():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            buttons[i][0].config(bg = "Green")
            buttons[i][1].config(bg="Green")
            buttons[i][2].config(bg="Green")
            return True
        elif buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
            buttons[0][i].config(bg="Green")
            buttons[1][i].config(bg="Green")
            buttons[2][i].config(bg="Green")
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="Green")
        buttons[1][1].config(bg="Green")
        buttons[2][2].config(bg="Green")
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="Green")
        buttons[1][1].config(bg="Green")
        buttons[2][0].config(bg="Green")
        return True
    elif empty_spaces() is False:
        for i in range(3):
            for j in range(3):
                buttons[i][j].config(bg="Yellow")
        return "Tie"
    else:
        return False


def empty_spaces():
    for i in range(3):
        for j in range(3):
            if buttons[i][j]['text'] == "":
                return True
    return False


def next_turn(row, column):
    global player
    if buttons[row][column]['text'] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[1]
                label.config(text=player+"'s turn")
            elif check_winner() is True:
                label.config(text=player + " wins")
            elif check_winner() == "Tie":
                label.config(text="TIE!")
        else:
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[0]
                label.config(text=player + "'s turn")
            elif check_winner() is True:
                label.config(text=player + " wins")
            elif check_winner() == "Tie":
                label.config(text="TIE!")


window = Tk()
window.title("Simple Tic Tac Toe")
window.config(background="#ff8c00")
for i in range(5):
    window.grid_rowconfigure(i, weight=1)
for j in range(3):
    window.grid_columnconfigure(j, weight=1)
players = ['x', 'o']
player = random.choice(players)
label = Label(window, text=player+"'s turn", font=("Ink Free", 40, "bold"), background="#ff8c00",
              foreground="#ffffff")
label.grid(row=0, columnspan=3)
reset_button = Button(window, text="Restart", font=("Ink Free", 30, "bold"),borderwidth=0,
                      command=new_game, background="#ff8c00", foreground="#ffffff",
                      activeforeground="#ff8c00", activebackground="#ffffff")
reset_button.grid(row=1, columnspan=3)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
for i in range(3):
    for j in range(3):
        buttons[i][j] = Button(window, text="", font=("Ink Free", 40, "bold"),
                               width=3, height=1, bg="#f8ccf9", fg="#7e4b8b",
                               command= lambda row=i, column=j: next_turn(row, column))
        buttons[i][j].grid(row=i+2, column=j, sticky="nesw")

window.mainloop()
