from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from art import logo

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

print(logo)
while quiz.still_has_questions():
    continue_toplay = input("Would you like to continue playing, Yes or No? ").lower()
    if continue_toplay == "no":
        break
    else:
        quiz.next_question()
print(f"\nYou've completed the quiz!\nYor final score was: {quiz.score} of {quiz.question_number}")
