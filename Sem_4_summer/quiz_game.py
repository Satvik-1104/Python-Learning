def new_game():
    questions = {
        "1. Who is the Prime minister of India?": "A",
        "2. Who is the Political Strategist ot Tactician of India?": "C",
        "3. Who invented Python?": "A",
        "4. Which datatype is immutable in Python?": "D"
    }

    options = [
        ['A: Narendra Modi', 'B: Abdul Kalam', 'C: Sarvepalli Radhakrishnan', 'D: Rajiv Gandhi'],
        ['A: Yogi Adityanath', 'B:  Akhilesh Yadav', 'C: Prashant Kishore', 'D: Arvind Kejriwal'],
        ['A: Guido van Rossum', 'B: Jack Dorsey', 'C: Grace Hopper', 'D: Richard Stallman'],
        ['A: List', 'B: Set', 'C: Dictionary', 'D: Tuple']
    ]
    your_answers = []
    correct_answers = 0
    question_number = 1
    for question in questions.keys():
        print(question)
        for i in options[question_number - 1]:
            print(i)
        your_answer = input("Answer: ").upper()
        correct_answers += check_answer(your_answer, questions[question])
        your_answers.append(your_answer)
        question_number += 1
    print("-------------------------------------------------------------------------------------------------------")
    print("Your answers: ", end="")
    for i in your_answers:
        print(i, end=" ")
    print()
    print("Answers: ", end="")
    for key, value in questions.items():
        print(value, end=" ")
    show_score(your_answers, correct_answers)


def play_again():
    response = input("Do you want to play again? (yes/no): ").upper()
    if response == 'YES':
        return  True
    else:
        return False


def check_answer(your_answer, answer):
    if your_answer == answer:
        print("Correct")
        return 1
    else:
        print("Wrong")
        return 0


def show_score(your_answers, correct_answers):
    print()
    print("Your score is: ", end="")
    total = len(your_answers)
    print(str(total))
    print(str(correct_answers))
    percentage = (correct_answers / total) * 100
    print(str(percentage) + "%")


new_game()
while play_again():
    print("-------------------------------------------------------------------------------------------------------")
    new_game()