from data import question_data
from question_model import Question
from quiz_brain import Quiz

question_bank = []
for question in question_data:
    text = question["text"]
    answer = question["answer"]
    new_question = Question(q_text=text, q_answer=answer)
    question_bank.append(new_question)

quiz = Quiz(question_bank)

while quiz.still_remain():
    quiz.next_question()

print(f"\nYour final score is {quiz.score}.\nCorrect answer: {quiz.score}.\nWrong answer  {len(question_bank) - quiz.score}")
