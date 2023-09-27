# ask user question
# check if the answer is correct
# check if we are at the end of the quiz

from exercices.quiz.question_model import Question


class QuizBrain:
    def __init__(self, questions) -> None:
        self.question_number = 0
        self.score = 0
        self.question_list = questions

    def check_answer(self, user_answer: str, correct_answer: str) -> None:
        if user_answer == correct_answer:
            self.score += 1
            msg = "right"
        else:
            msg = "wrong"
        self.question_number += 1
        print(f"You are {msg}! score: {self.score}/{self.question_number}")


    def ask_questions(self):
        while self.question_number < len(self.question_list):
            pos = self.question_number
            question = self.question_list[pos]
            user_answer = input(f"Q{pos} {question.text} (True/False) ").lower()
            correct_answer = question.answer.lower()
            self.check_answer(user_answer, correct_answer)
