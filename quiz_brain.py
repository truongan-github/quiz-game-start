class Quiz:
    def __init__(self, question_list):
        self.score = 0
        self.question_list = question_list
        self.question_number = 0

    def still_remain(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(answer=answer, current_question=current_question.answer)

    def check_answer(self, answer, current_question):
        if answer.lower() == current_question.lower():
            self.score += 1
            print("Correct!")
        else:
            print("Wrong answer!")

        print(f"Your score is {self.score}/12\n")