import random

choice = input("Do you want to play a 5-point ROCK, PAPER, SCISSOR Game with AI (yes/no)?: ").lower()
if choice == 'yes':
    choices = {'rock': 1, 'paper': 2, 'scissors': 3}
    player_points = int(0)
    computer_points = int(0)

    while computer_points < 5 and player_points < 5:
        computer = random.choice(list(choices.keys()))
        player = None
        while player not in choices.values():
            player = int(input("Rock (1), Paper (2) or Scissors (3)?: "))
        player = [key for key, value in choices.items() if value == player][0]
        if computer == player:
            print("Tie !")
        elif player == 'rock':
            if computer == 'scissors':
                player_points += 1
            elif computer == 'paper':
                computer_points += 1

        elif player == 'paper':
            if computer == 'rock':
                player_points += 1
            elif computer == 'scissors':
                computer_points += 1

        elif player == 'scissors':
            if computer == 'paper':
                player_points += 1
            elif computer == 'rock':
                computer_points += 1

        print("Computer: " + computer)
        print("Player: " + player)
        print("Computer: " + str(computer_points) + "    You: " + str(player_points))
        print()

    if computer_points == 5:
        print("You lose : (")
        print("Try again next time")
    else:
        print("Yay!! You Win !!!")

else:
    print("Sare DENGEY")