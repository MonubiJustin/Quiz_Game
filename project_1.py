from database import question_bank
from database import options
print('**********************************************')
print('Welcome to my quiz game')
score = 0
def check_answer(answer, correct_answer):
    if answer == correct_answer:
        return True
    else:
        return False
for question_num in range(len(question_bank)):
    # print('**********************************************')
    print(question_bank[question_num]['text'])
    for i in options[question_num]:
        print(i)
    guess = input("Enter (A/B/C/D): ").upper()
    Is_correct=check_answer(guess, question_bank[question_num]['answer'])
    if Is_correct:
        score += 1
        print('Correct answer')
    else:
        print('Incorrect answer')
        print(f"The correct answer is: {question_bank[question_num]['answer']}")
    print(f"Your current score is {score}/{question_num+1}")
print(f"You have given {score} correct answers.")
print(f"Your score is {(score/len(question_bank))*100}%")