import os
from database_2 import question_bank
from database_2 import options
import math

print('****************************************')
print('****** Welcome to my quiz game!!! ******')

def check_answer(guessed_answer, correct_answer):
    return guessed_answer == correct_answer

score = 0

for question_num in range(len(question_bank)):
    print('=============================================================================')
    print(question_bank[question_num]['text'])
    for i in options[question_num]:
        print(f'\t{i}')

    guess = input('Enter (A/B/C/D): ').upper()
    Is_correct = check_answer(guess, question_bank[question_num]['answer'])

    if Is_correct:
        print('>>>>>> Correct answer! <<<<<<')
        score += 1
    else:
        print('>>>>>> Incorrect answer! <<<<<<')
        print(f"The correct answer is: {question_bank[question_num]['answer']}")

    print(f"Your score is {score}/{question_num + 1}")

    # Prompt the user to continue or quit
    if question_num < len(question_bank) - 1:
        choice = input("Press 'Enter' to continue or type 'q' to quit: ")
        if choice.lower() == 'q':
            break

    # Clear the console
    os.system('cls')  # Use 'clear' for Unix-based systems

print(f'\nYour final score is {score}/{len(question_bank)}')
print(f'Your percentage score is {math.ceil((score / len(question_bank)) * 100)}%')
