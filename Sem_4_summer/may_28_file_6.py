from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 100
BODY_PARTS = 3
SNAKE_COLOUR = "#0050ff"
BACKGROUND_COLOUR = "#300500"
FOOD_COLOUR = "#b8ff00"
SPACE_SIZE = 50


class Food:
    def __init__(self):
        x = random.randint(0, int(GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, int(GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                           fill=FOOD_COLOUR, tags="food")


class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.squares = []
        self.coordinates = []

        for i in range(BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE,
                                             y + SPACE_SIZE, fill=SNAKE_COLOUR)
            self.squares.append(square)


def check_collisions(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False


def change_direction(new_direction):
    global direction
    if new_direction == "left":
        if direction != "right":
            direction = new_direction
    if new_direction == "right":
        if direction != "left":
            direction = new_direction
    if new_direction == "up":
        if direction != "down":
            direction = new_direction
    if new_direction == "down":
        if direction != "up":
            direction = new_direction


def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       text="GAME OVER\nSCORE: " + str(score),
                       font=("Consolas", 45), fill="#00ffd0")

def next_turn(snake, food):
    global score
    x, y = snake.coordinates[0]
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE

    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE,
                                     y + SPACE_SIZE, fill=SNAKE_COLOUR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        score += 1
        label.config(text="Score: " + str(score))
        canvas.delete("food")
        food = Food()

    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake) is True:
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)


window = Tk()
window.title("SNAKE GAME")
window.resizable(False, False)

score = 0
direction = "down"

label = Label(window, text="Score: " + str(score), font=("Consolas", 40))
label.pack()

canvas = Canvas(window, background=BACKGROUND_COLOUR, width=GAME_WIDTH, height=GAME_HEIGHT)
canvas.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width - window_width) / 2)
y = int((screen_height - window_height) / 2)
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, 0))

window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Left>", lambda event: change_direction("left"))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()
