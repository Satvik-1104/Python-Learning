# simple quiz game


def new_game():
    guesses = []
    question_num = 1
    for key in questions:
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter your answer: ").upper()
        guesses.append(guess)
        question_num += 1
        print("-----------------------------------------------------------")
    check_answers(guesses)


def check_answers(guesses):
    correct_answers = 0
    answers = [value for key, value in questions.items()]
    for i in range(len(answers)):
        if guesses[i] == answers[i]:
            correct_answers += 1
    display_score(guesses, answers, correct_answers)


def display_score(guesses, answers, correct_answers):
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
    print("Answers: ", end="")
    for j in answers:
        print(j, end=" ")
    score = (correct_answers/len(answers)) * 100
    print()
    print("Score: " + str(score))
    play_again()


def play_again():
    response = input("Do you want to play again? (YES?NO): ").upper()
    if response == "YES":
        new_game()
    else:
        print("Bye Bye")


questions = {
    "What is my name?": "C",
    "Where am I studying?": "A",
    "What is my CPI?": "A",
    "Where is my Native Place?": "D"
}

options = [
    ['A. Pranav', 'B. Divya', 'C. Satvik', 'D. Jignesh'],
    ['A. IIITG', 'B. IITB', 'C. IITV', 'D. IIITN'],
    ['A. 8.10', 'B. 8.17', 'C. 6.97', 'D. 6.46'],
    ['A. Macharla', 'B. Guduru', 'C. Vizag', 'D. Pithapuram'],
]

new_game()
