# rock, paper, scissors game

import random

choices = ["rock", "paper", "scissors"]

while True:
    player = None
    while player not in choices:
        player = input("Enter your choice: ").lower()
    computer = random.choice(choices)

    if player == computer:
        print("Player: " + player)
        print("Computer: " + computer)
        print("TIE!")

    elif player == "rock":
        if computer == "paper":
            print("Player: " + player)
            print("Computer: " + computer)
            print("YOU LOSE!")
        elif computer == "scissors":
            print("Player: " + player)
            print("Computer: " + computer)
            print("YOU WIN!")

    elif player == "paper":
        if computer == "scissors":
            print("Player: " + player)
            print("Computer: " + computer)
            print("YOU LOSE!")
        elif computer == "rock":
            print("Player: " + player)
            print("Computer: " + computer)
            print("YOU WIN!")

    elif player == "scissors":
        if computer == "rock":
            print("Player: " + player)
            print("Computer: " + computer)
            print("YOU LOSE!")
        elif computer == "paper":
            print("Player: " + player)
            print("Computer: " + computer)
            print("YOU WIN!")

    interest = input("Do you want to continue?(yes/no): ").lower()
    if interest != 'yes':
        break
print("Bye bye")
